from flask import Flask, jsonify, send_file, abort, request
from flask_cors import CORS

from db_helper import DB_HELPER


db = DB_HELPER()

app = Flask(__name__)
CORS(app)



@app.route('/ping')
def ping_pong():
    """
    Функция для проверки работоспособности серверной части проекта
    """
    return jsonify('pong')


@app.route('/api/url', methods=['POST'])
def create_short_url():
    if not request.json:
        abort(400)  # ошибка 400 если нет тела запроса
    url_obj = {
        'original_url': request.json.get('original_url')
    }
