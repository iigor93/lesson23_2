from flask import request, abort
from marshmallow_dataclass import class_schema
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CommandData:
    regex: str = ''
    filename: str = 'apache_logs.txt'
    filter: str = ''
    unique: bool = False
    limit: int = 10
    sort: str = 'asc'
    column: int = field(default=-1, metadata={"data_key": "map"})


def get_dict() -> Optional[CommandData]:
    """Получаем из запроса команды"""
    commands = ('filter', 'unique', 'map', 'limit', 'sort', 'regex', 'filename')
    if request.is_json:
        data = request.json
    elif request.form.get('query'):
        data_received = request.form.get('query').split('|')
        data = {}

        for item in data_received:
            temp_val = item.split(':')
            try:
                data[temp_val[0]] = temp_val[1]
            except IndexError:
                data[temp_val[0]] = True
    else:
        return abort(400)

    for item in commands:
        if item in data:
            command_data_schema = class_schema(CommandData)
            commands_data = command_data_schema().load(data)
            return commands_data

    return abort(400)
