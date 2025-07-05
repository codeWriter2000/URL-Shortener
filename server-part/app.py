from flask import Flask, jsonify, abort, request, redirect
from flask_cors import CORS
import json

import url
from url import URL
from utils import get_qr_bs64

from config import HOST, PORT


app = Flask(__name__)
CORS(app)

host = HOST
port = PORT

url_template = "http://{}:{}/{}"

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
        abort(500)  # Internal server error
    return jsonify(res)


@app.route('/api/url', methods=['POST'])
def create_short_url():
    if not request.json:
        abort(400)  # Bad request
    req = {
        'original_url': request.json.get('original_url')
    }

    url_obj = URL.generate_new(req['original_url'])
    qr_b64 = get_qr_bs64(url_template.format(
        host,
        port,
        url_obj.short_token
    ))

    data_2_res = url_obj.url_2_dict()
    data_2_res['qrcode'] = qr_b64

    return jsonify(data_2_res)


@app.route('/<string:token>', methods=['GET'])
def go_to(token: str):
    original_url = URL.get_original_by_token(token)
    if not original_url:
        abort(404)  # Not Found - если передан некорректный токен или он уже не действителен
    URL.log_url_data(original_url)  # логируем информацию
    return redirect(original_url)


@app.route('/api/nearest/<int:count>', methods=['GET'])
def get_nearest_urls(count):
    if count not in url.approved_url_cnt:
        abort(400)  # Bad request
    return jsonify(URL.get_nearest_urls(count))


@app.route('/api/distinct_origins_from_storage', methods=['GET'])
def get_origins_stat():
    origin_data = URL.distinct_origins()
    return jsonify(origin_data)


@app.route('/api/origin_statistic_by_logs', methods=['GET'])
def get_origin_stat_by_logs():
    origin_visits = URL.origin_statistic_by_logs()
    return jsonify(origin_visits)
