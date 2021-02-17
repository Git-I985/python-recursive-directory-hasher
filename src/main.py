from os import path
from hasher import RecursiveDirectoriesHasher, EachDirectoryHasher
# GUI
import tkinter as tk
from tkinter import filedialog
from wconfigs import configs
from widgets import Button, CheckButton, Input, Label


def print_arr_lbl(data):
    print(*data, sep='\n', end='\n\n')


def save_to_xlsx(file, columns, data):
    from openpyxl import Workbook
    from openpyxl.styles import Font

    wb = Workbook()
    ws = wb.active
    ws.title = "export"
    ws.append(columns)

    for cell in ws["1:1"]:
        cell.font = Font(bold=True)

    for row in data:
        ws.append(row)

    wb.save(file)


def exclude_common_path(data: list):
    common = path.commonpath(row[0] for row in data)

    def common_path_mapper(row):
        row[0] = path.relpath(row[0], common)
        return row

    return list(map(common_path_mapper, data))


def edh_output_handler(data, directory):

    # Обрабатывает пути к файлам
    def basename_path_mapper(data: dict):
        data['file'] = path.basename(data['file'])
        return data

    def serial_number_mapper(data: dict):
        def get_short_year():
            from datetime import datetime
            now = datetime.now()
            year = str(now.year)
            return year[len(year) // 2:]

        serial_number = data['serial_number']
        serial_number = 'F-{}.{}'.format(get_short_year(),
                                         '/'.join(map(lambda x: str(x + 1), serial_number)))

        data["serial_number"] = serial_number

        return data

    data = list(map(serial_number_mapper, data))
    data = list(map(basename_path_mapper, data))
    data = list(map(lambda item: list(item.values()), data))
    print(data, sep='\n', end='\n\n')

    filename = path.basename(path.normpath(directory)) + '.xlsx'
    save_to_xlsx('./export/' + filename,
                 ['Уч №', 'Имя\Путь', 'md5', 'sha1'], data)


def run():

    # Получение путей
    directory = input_folder.get()
    export = input_export.get()

    # Очистка полей ввода путей
    input_export.clear()
    input_folder.clear()

    data = []

    # Если установлен флажок "отдельный файл для каждой папки"
    if is_separated.get():
        edh = EachDirectoryHasher(directory)
        edh.start(edh_output_handler)

        return

    rdh = RecursiveDirectoriesHasher(directory)
    rdh.start(data.append)

    # Убрать совпадающую часть пути файла (все от корня до папки)
    data = exclude_common_path(data)

    # Сохранить в excel
    save_to_xlsx(export, ['Имя\Путь', 'md5', 'sha1'], data)


def select_folder():
    directory = filedialog.askdirectory(title="Select hashing directory")
    if directory:
        input_folder.setText(directory)


def select_export():
    file = filedialog.asksaveasfile("w", title="Choose export file")
    input_export.setText(file.name)
    file.close()


window = tk.Tk()
window.title('RecursiveDirectoryHasher')
window.resizable(False, False)


Label().set_config(configs['LabelFolderPath'])
Label().set_config(configs["LabelExportPath"])


btn_select_folder = Button().set_config(configs["ButtonSelectFolder"])
btn_select_folder.onclick = select_folder

btn_select_export = Button().set_config(configs["ButtonSelectExport"])
btn_select_export.onclick = select_export


btn_run = Button().set_config(configs["ButtonRun"])
btn_run.onclick = run

is_separated = tk.BooleanVar()
is_separated.set(1)
checkbox_separated = CheckButton(variable=is_separated, onvalue=1, offvalue=0,).set_config(
    configs["CheckButtonSeparated"])

input_folder = Input().set_config(configs["EntrySelectFolder"])
input_export = Input().set_config(configs["EntrySelectExport"])

window.mainloop()
