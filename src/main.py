from tkinter import filedialog
import tkinter as tk
from cswriter import CsvWriter
# GUI
from wconfigs import configs
from widgets import Input, Label, Button
from hasher import RecursiveDirectoriesHasher


class App():
    def __init__(self):
        pass


def select_folder():
    directory = filedialog.askdirectory(title="Select hashing directory")
    if directory:
        input_folder.setText(directory)


def select_export():
    file = filedialog.asksaveasfile(
        "w", filetypes=[("Csv files", '*.csv')],
        title="Choose export file")
    input_export.setText(file.name)
    file.close()


def run():
    directory = input_folder.get()
    export = input_export.get()
    input_export.clear()
    input_folder.clear()
    cw = CsvWriter(export)
    cw.set_columns(['File', 'MD5', 'SHA1'])
    rdh = RecursiveDirectoriesHasher(directory)
    rdh.start(cw.write_row)
    cw.save()


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

input_folder = Input().set_config(configs["EntrySelectFolder"])
input_export = Input().set_config(configs["EntrySelectExport"])

window.mainloop()
