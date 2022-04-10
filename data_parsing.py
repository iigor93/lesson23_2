from flask import request, abort


def get_dict():
    """Получаем из запроса команды"""
    commands = ('filter', 'unique', 'map', 'limit', 'sort', 'filename')
    if request.is_json:
        data = request.json
    else:
        data_received = request.form.get('query').split('|')
        data = {}

        for item in data_received:
            temp_val = item.split(':')
            try:
                data[temp_val[0]] = temp_val[1]
            except IndexError:
                data[temp_val[0]] = True
    for item in commands:
        if item in data:
            return data

    return abort(400)
