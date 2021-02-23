from os import path
from hasher import RecursiveDirectoriesHasher, EachDirectoryHasher
# GUI
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
from wconfigs import configs
from widgets import Button, CheckButton, Input, Label
# Hashing
from handlers import edh_output_handler, rdh_output_handler
from hasher import EachDirectoryHasher, RecursiveDirectoriesHasher
import functools

# TODO: обработка ошибок и вывод уведомлений


def run():
    # Получение и очистка полей
    directory = input_folder.get()
    export = input_export.get()

    if not directory:
        gui_execution_fail('Выберете хешируемую директорию')
        return

    if not export:
        gui_execution_fail('Выберете путь экспорта')
        return

    btn_run.set_config(configs['ButtonRunInProcess'])

    try:
        # Hashing
        hasher = EachDirectoryHasher(directory) if is_separated.get(
        ) else RecursiveDirectoriesHasher(directory)
        handler = edh_output_handler if is_separated.get() else rdh_output_handler
        hasher.start(functools.partial(handler, export=export))
    except Exception as e:
        gui_execution_fail(e)
    else:
        input_folder.clear()
        input_export.clear()
        gui_execution_success()
    finally:
        btn_run.set_config(configs['ButtonRun'])

# ====================================================
#
#   ####    ##   ##  ##
#  ##       ##   ##  ##
#  ##  ###  ##   ##  ##
#  ##   ##  ##   ##  ##
#   ####     #####   ##
#
# ====================================================


def gui_execution_success():
    mb.showinfo(title='Результат выполнения',
                message='Выполнение завершено успешно')


def gui_execution_fail(msg):
    mb.showerror(title='Ошибка', message=msg)

# gui_execution_success()


def select_folder():
    directory = filedialog.askdirectory(title="Select hashing directory")
    if directory:
        input_folder.setText(directory)


def select_export_file():
    file = filedialog.asksaveasfile(
        "w", title="Choose export file", filetypes=[("Excel files", ".xlsx .xls")])
    if file:
        filename, extension = path.splitext(file.name)
        if extension in [".xlsx", ".xls"]:
            input_export.setText(file.name)
            file.close()


def select_export_directory():
    directory = filedialog.askdirectory(title="Select export directory")
    if directory:
        input_export.setText(directory)


def on_checkbox_change():
    if is_separated.get():
        btn_select_export.onclick = select_export_directory
        return
    btn_select_export.onclick = select_export_file


window = tk.Tk()
window.title('RecursiveDirectoryHasher')
window.resizable(False, False)


Label().set_config(configs['LabelFolderPath'])
Label().set_config(configs["LabelExportPath"])


btn_select_folder = Button().set_config(configs["ButtonSelectFolder"])
btn_select_folder.onclick = select_folder

btn_select_export = Button().set_config(configs["ButtonSelectExport"])
btn_select_export.onclick = select_export_file


btn_run = Button().set_config(configs["ButtonRun"])
btn_run.onclick = run

is_separated = tk.BooleanVar()
is_separated.set(0)
checkbox_separated = CheckButton(variable=is_separated, onvalue=1, offvalue=0, command=on_checkbox_change).set_config(
    configs["CheckButtonSeparated"])

input_folder = Input().set_config(configs["EntrySelectFolder"])
input_export = Input().set_config(configs["EntrySelectExport"])

window.mainloop()
