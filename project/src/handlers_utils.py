from os import path


def exclude_common_path(data: list, key: str = None):
    common = path.commonpath(row[key] for row in data)

    def common_path_mapper(row):
        row[key] = path.relpath(row[key], common)
        return row

    return list(map(common_path_mapper, data))


def basename_path_mapper(data: dict, key: str = None):
    data[key] = path.basename(data[key])
    return data


def serial_number_mapper(data: dict, key: str = None):
    from datetime import datetime

    def get_short_year():
        now = datetime.now()
        year = str(now.year)

        return year[len(year) // 2:]

    serial_number = data[key]
    serial_number = 'Е-{}.{}'.format(get_short_year(),
                                     '/'.join(map(lambda x: str(x + 1), serial_number)))

    data[key] = serial_number

    return data
