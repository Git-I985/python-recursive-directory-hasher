from tkinter import filedialog
import tkinter as tk
from cswriter import CsvWriter
# GUI
from wconfigs import configs
from widgets import Input, Label, Button
from hasher import RecursiveDirectoryHasher


class App():
    def __init__(self):
        pass


def select_folder():
    selectedDirectory = filedialog.askdirectory(
        title="Select hashing directory")
    if selectedDirectory:
        inputExport.setText(selectedDirectory)


def select_export():
    selectedExport = filedialog.asksaveasfilename(
        filetypes=[("Csv files", '*.csv')], title="Choose export file")
    if selectedExport:
        print(selectedExport)


def run():
    cw = CsvWriter('exports.csv')
    cw.set_columns(['File', 'MD5', 'SHA1'])
    rfh = RecursiveDirectoryHasher(pathInput.get())
    rfh.start(cw.write_row)
    pathInput.delete(0, len(pathInput.get()))
    cw.save()


window = tk.Tk()
window.title('RecursiveDirectoryHasher')
window.resizable(False, False)


Label().setConfig(configs['LabelFolderPath'])
Label().setConfig(configs["LabelExportPath"])

btn_select_folder = Button()
btn_select_folder.onclick = select_folder
btn_select_folder.setConfig(configs["ButtonSelectFolder"])

btn_select_export =
Button().setConfig(configs["ButtonSelectExport"])
Button().setConfig(configs["ButtonRun"])

inputFolder = Input()
inputFolder.setConfig(configs["EntrySelectFolder"])
inputExport = Input().setConfig(configs["EntrySelectExport"])

window.mainloop()
