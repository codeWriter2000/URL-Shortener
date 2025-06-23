from flask import Flask, jsonify, send_file, abort, request, redirect
from flask_cors import CORS

from url import URL


app = Flask(__name__)
CORS(app)


@app.route('/ping')
def ping_pong():
    """
    Функция для проверки работоспособности серверной части проекта
    """
    return jsonify('pong')


@app.route('/api/manual_url_deactivation')
def url_deactivate():
    res = URL.weekly_deactivate()
    if not res:
        abort(505)  # Internal server error
    return jsonify(res)


@app.route('/api/url', methods=['POST'])
def create_short_url():
    if not request.json:
        abort(400)  # Bad request
    req = {
        'original_url': request.json.get('original_url')
    }
    url_obj = URL.generate_new(req['original_url'])
    return jsonify(url_obj.url_2_json())


@app.route('/<string:token>', methods=['GET'])
def go_to(token: str):
    original_url = URL.get_original_by_token(token)
    if not original_url:
        abort(404)  # Not Found - если передан некорректный токен или он уже не действителен
    return redirect(original_url)
