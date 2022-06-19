import os
from typing import Type, Any

from werkzeug.exceptions import BadRequest

from utils import build_query
from flask import Flask, request, Response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query() -> tuple[Type[BadRequest], int] | Any:
    # нужно взять код из предыдущего ДЗ
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py
    try:
        cmd1 = request.args['cmd1']
        cmd2 = request.args['cmd2']
        value1 = request.args['value1']
        value2 = request.args['value2']
        file_name = request.args['file_name']
    except:
        raise BadRequest

    path_file = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(path_file):
        raise BadRequest(description=f"{file_name} was not found")

    with open(path_file) as f:
        res = build_query(f, cmd1, value1)
        res = build_query(res, cmd2, value2)
        content = '\n'.join(res)
    return app.response_class(content, content_type="text/plain")
