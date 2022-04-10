import os
from flask import abort


def file_read(commands):
    """Читаем файл согласно командам из запроса"""

    user_filter = commands.get('filter') if commands.get('filter') else ''
    unique = True if commands.get('unique') else False
    limit = int(commands.get('limit')) if commands.get('limit') else 10
    column = int(commands.get('map')) if commands.get('map') is not None else -1
    reverse = True if commands.get('sort') == 'desc' else False

    filename = commands.get('filename') if commands.get('filename') else 'apache_logs.txt'
    folder = 'data//'
    files = os.listdir(folder)

    if filename not in files:
        return abort(400)

    filename = folder + filename

    f = (row for row in open(filename))

    if column >= 0:
        lines = filter(lambda string: user_filter in string.split(' ')[column], f)
        map_lines = (thing.split(' ')[column] for thing in lines)
    else:
        map_lines = filter(lambda string: user_filter in string, f)

    if unique:
        map_lines = list(set(map_lines))

    if limit > 0:
        map_lines = list(map_lines)[: limit]

    return_list = sorted(map_lines, reverse=reverse)

    return return_list
