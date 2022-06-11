import os
from flask import Flask, request
from werkzeug.exceptions import BadRequest
from utils import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    try:
        cmd1 = request.args['cmd1']
        cmd2 = request.args['cmd2']
        value1 = request.args['value1']
        value2 = request.args['value2']
        file_name = request.args['file_name']

    except:
        return BadRequest, 400

    path_file = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(path_file):
        return BadRequest, 400

    with open(path_file) as f:
        res = build_query(f, cmd1, value1)
        res = build_query(res, cmd2, value2)
        res = '\n'.join(res)

    return app.response_class(res, content_type="text/plain")




# получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
# проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
# с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
# вернуть пользователю сформированный результат