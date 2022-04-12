import os
import re
from flask import abort
from data_parsing import CommandData
from typing import List, Optional


def file_read(commands_data: CommandData) -> Optional[List]:
    """Читаем файл согласно командам из запроса"""

    folder = 'data//'
    files = os.listdir(folder)

    if commands_data.filename not in files:
        return abort(400)

    filename = folder + commands_data.filename

    f = (row for row in open(filename))

    if commands_data.column >= 0:
        lines = filter(lambda string: commands_data.filter in string.split(' ')[commands_data.column], f)
        map_lines = (thing.split(' ')[commands_data.column] for thing in lines)
    else:
        map_lines = filter(lambda string: commands_data.filter in string, f)  # type: ignore

    if commands_data.regex != '':
        map_lines = [line for line in map_lines if re.search(commands_data.regex, line)]  # type: ignore

    if commands_data.unique:
        map_lines = list(set(map_lines))  # type: ignore

    if commands_data.limit > 0:
        map_lines = list(map_lines)[: commands_data.limit]  # type: ignore

    reverse = True if commands_data.sort == 'desc' else False
    return_list = sorted(map_lines, reverse=reverse)

    return return_list
