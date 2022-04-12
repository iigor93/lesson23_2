import os

from flask import Flask, request, jsonify
from data_parsing import get_dict
from file_read import file_read


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['GET', 'POST'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    if request.method == 'GET':
        post_example = 'JSON - {"filter":"GET","map":0, "unique":"None", "sort":"desc"}\r\n' \
                       'FORM POST - key=query, value=filter:GET|map:0|unique|sort:desc'
        return post_example, 200

    if request.method == 'POST':
        commands_data = get_dict()
        data = file_read(commands_data)

        return jsonify(data)


if __name__ == '__main__':
    app.run()
