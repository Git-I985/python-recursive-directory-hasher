import functools  # небольшая утилита которая облегчает работу с функциями
from os import path  # модуль path библиотеки os, для работы с путями в файловой системе
# Библиотека Tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
# Свои файлы (для кнопок, полей итд)
from wconfigs import configs
from widgets import Button, CheckButton, Input, Label
# Свои файлы (для хеширования)
from hasher import RecursiveDirectoriesHasher, EachDirectoryHasher
from handlers import edh_output_handler, rdh_output_handler
from hasher import EachDirectoryHasher, RecursiveDirectoriesHasher
# Cвой файл сверки с excel файлов
from verifier import verify


def run():  # Функция вызываемая при нажатии на большую синюю кнопку run
    # Получение и очистка полей
    directory = input_folder.get()
    export = input_export.get()

    # Если не указана директория с которой надо работать,
    # тогда выдать сообщение об ошибке и выйти из функции до следущего вызова
    if not directory:
        gui_execution_fail('Выберете хешируемую директорию')
        return

    # Если не указана директория в которую надо выгружать excel файлы, или файл эксопрта в случае одного файла,
    # тогда выдать сообщение об ошибке и выйти из функции до следущего вызова
    if not export:
        gui_execution_fail('Выберете путь экспорта')
        return

    # Перевести внешний вид кнопки в режим загрузки
    btn_run.set_config(configs['ButtonRunInProcess'])

    # Обработка ошибок (что-бы программа не вылетала в случае ошибки, а просто останавливалась)
    try:
        # Если не включен мод проверки тогда выполнить хеширование
        if not is_verify_mode.get():
            # Выбор одного из двух хешеров
            hasher = EachDirectoryHasher(directory) if is_separated.get(
            ) else RecursiveDirectoriesHasher(directory)
            # Выбор одного из двух обработчиков вывода хешеров
            handler = edh_output_handler if is_separated.get() else rdh_output_handler
            # Зупуск процесса
            hasher.start(functools.partial(handler, export=export))
        else:
            # Иначе запустить функцию сверки excel файла с катологом, функция из файла verifier.py
            result = verify(directory, export)
            if result:
                gui_execution_success(
                    'Данные файла совпадают с реальными данными директории')
            else:
                gui_execution_fail(
                    'Данные файла не совпадают с реальными данными директории')
            return
    except Exception as e:
        # Если ошибка, тогда выдать сообщение об ошибке в диалоговом окне
        gui_execution_fail(e)
    else:
        # Если успешно, тогда очистить поля путей и вывести сообщение об успешном выполнении
        input_folder.clear()
        input_export.clear()
        gui_execution_success()
    finally:
        # В любом случае вернуть кнопке обычный вид
        btn_run.set_config(configs['ButtonRun'])

#
#
# Дальше идет описание интерфейса


def gui_execution_success(msg='Выполнение завершено успешно'):
    # Функция уведомления об успешном завершении
    mb.showinfo(title='Результат выполнения',
                message=msg)


def gui_execution_fail(msg):
    # Функция уведомления об ошибке при выполнении программы
    mb.showerror(title='Ошибка', message=msg)


def select_folder():
    # Функция вызываемая при нажатии на кнопку выбора директории которую надо хешировать
    directory = filedialog.askdirectory(title="Select hashing directory")
    if directory:
        input_folder.setText(directory)


def select_export_file():
    # Функция вызываемая при нажатии на кнопку выбора файла экспорта (в режиме "все в один файл")
    file = filedialog.askopenfilename(title="Choose export file", filetypes=[
        ("Excel files", ".xlsx .xls")])
    if file:
        input_export.setText(file)


def select_export_directory():
    # Функция вызываемая при нажатии на кнопку выбора директории экспорта (в режиме отедльный файл для каждой папки)
    directory = filedialog.askdirectory(title="Select export directory")
    if directory:
        input_export.setText(directory)


def on_checkbox_change():
    # Флажок включения режима excel файла для каждой директории
    is_verify_mode.set(0)
    # Текст кнопки
    if is_verify_mode.get():
        btn_select_export.configure(text="Export verify")
    else:
        btn_select_export.configure(text="Select export")
    btn_select_export.onclick = (
        select_export_directory if is_separated.get() else select_export_file)


def on_verify_mode_checkbox_change():
    # Флажок включения режима проверки целостности файлов по excel таблице
    # Текст кнопки
    if is_verify_mode.get():
        btn_select_export.configure(text="Export verify")
    else:
        btn_select_export.configure(text="Select export")

    is_separated.set(0)
    btn_select_export.onclick = select_export_file


window = tk.Tk()  # само окно программы
window.title('RecursiveDirectoryHasher')  # заголовок окна
window.resizable(False, False)  # запрет на изменение размеров окна

Label().set_config(configs['LabelFolderPath'])  # подпись к полю ввода 1
Label().set_config(configs["LabelExportPath"])  # подпись к полю ввода 2

# Кнопка выбора рабочей папки
btn_select_folder = Button().set_config(configs["ButtonSelectFolder"])
btn_select_folder.onclick = select_folder

# Кнопка выбора файла/директории экспорта
btn_select_export = Button().set_config(configs["ButtonSelectExport"])
btn_select_export.onclick = select_export_file

# Большая синяя кнопка run
btn_run = Button().set_config(configs["ButtonRun"])
btn_run.onclick = run

# Флажок 1
is_separated = tk.BooleanVar()
is_separated.set(0)
checkbox_separated = CheckButton(variable=is_separated, onvalue=1, offvalue=0, command=on_checkbox_change).set_config(
    configs["CheckButtonSeparated"])

# Флажок 2
is_verify_mode = tk.BooleanVar()
is_verify_mode.set(0)
checkbox_verify = CheckButton(variable=is_verify_mode, onvalue=1, offvalue=0, command=on_verify_mode_checkbox_change).set_config(
    configs["CheckButtonVerify"])

# Поля ввода путей (заполняются автоматически)
input_folder = Input().set_config(configs["EntrySelectFolder"])
input_export = Input().set_config(configs["EntrySelectExport"])

# Команда запуска интерфейса
window.mainloop()
