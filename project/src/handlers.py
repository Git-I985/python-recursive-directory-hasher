from handlers_utils import serial_number_mapper, basename_path_mapper, exclude_common_path
from xlsx import save_to_xlsx
import functools
from os import path


def dict_to_list(data: dict):
    return list(map(lambda item: list(item.values()), data))


def edh_output_handler(data, directory, export=None):
    # Обрабатывает каждую запись, меняет порядковые номера, обрабатывает пути к файлам
    data = list(map(functools.partial(
        serial_number_mapper, key="serial_number"), data))
    data = list(map(functools.partial(
        basename_path_mapper, key="file"), data))
    # Преобразует в массив
    data = dict_to_list(data)

    filename = path.basename(path.normpath(directory)) + '.xlsx'
    export = path.normpath(path.join(export, filename))
    save_to_xlsx(export, ['Уч №', 'Имя\Путь', 'md5', 'sha1'], data)


def rdh_output_handler(data, export=None, xlsx_mode=True):
    data = list(map(functools.partial(
        serial_number_mapper, key="serial_number"), data))
    data = exclude_common_path(data, key="file")
    data = dict_to_list(data)
    if not xlsx_mode:
        return data
    save_to_xlsx(export, ['Уч №', 'Имя\Путь', 'md5', 'sha1'], data)
