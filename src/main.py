from tkinter import filedialog, N, S, W, E
import tkinter as tk
from cswriter import CsvWriter
# GUI
from wconfigs import configs
from widgets import Input, Label, Button
from hasher import RecursiveDirectoryHasher



def select_folder():
    selectedDirectory = filedialog.askdirectory(title="Select hashing directory")
    if selectedDirectory:
        input_set_path(pathInput, selectedDirectory)
        
def select_export():
    selectedExport = filedialog.asksaveasfilename(filetypes=[("Csv files", '*.csv')], title="Choose export file")
    if selectedExport:
        print(selectedExport)

def run():
    cw = CsvWriter('exports.csv')
    cw.set_columns(['File', 'MD5', 'SHA1'])
    rfh = RecursiveDirectoryHasher(pathInput.get())
    rfh.start(cw.write_row)
    pathInput.delete(0, len(pathInput.get()))
    cw.save()

def test():
    print('hi ebat')

window = tk.Tk()
window.title('RecursiveDirectoryHasher')
window.resizable(False, False)

# Labels
Label().setConfig(configs['LabelFolderPath'])
Label().setConfig(configs["LabelExportPath"])

# Buttons
Button(command=test).setConfig(configs["ButtonSelectFolder"])
Button(command=test).setConfig(configs["ButtonSelectExport"])
Button(command=test).setConfig(configs["ButtonRun"])

# Inputs
Input().setConfig(configs["EntrySelectFolder"])
Input().setConfig(configs["EntrySelectExport"])

window.mainloop()