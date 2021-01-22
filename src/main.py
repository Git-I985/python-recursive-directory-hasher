import time, hashlib, os, typing
from rich.console import Console
from rich.table import Column, Table
from tkinter import filedialog, N, S, W, E
import tkinter as tk
# Self classes
from args import getArgs
from CsvWriter import CsvWriter


class RecursiveDirectoryHasher():
    def __init__(self, path: str):
        path = os.path.normpath(path)
        if not os.path.isdir(path):
            exit(f'{path} is not directory')
        self.path = path

    def get_hash(self, file: typing.BinaryIO):
        md5,sha1 = hashlib.md5(), hashlib.sha1()
        buf = file.read()
        md5.update(buf)
        file.close()
        sha1.update(buf)
        return md5.hexdigest(), sha1.hexdigest()

    def start(self, callback):
        for path, dirs, files in os.walk(self.path):
            for file in files:
                file = os.path.normpath(path + os.sep + file)
                md5, sha1 = self.get_hash(open(file, 'rb'))
                callback([file, md5, sha1])

def selectFolder():
    selectedDirectory = filedialog.askdirectory()
    if selectedDirectory:
        pathInput.delete(0, len(pathInput.get()))
        pathInput.insert(0, selectedDirectory)

def run():
    cw = CsvWriter('exports.csv')
    cw.set_columns(['File', 'MD5', 'SHA1'])
    rfh = RecursiveDirectoryHasher(pathInput.get())
    rfh.start(cw.write_row)
    pathInput.delete(0, len(pathInput.get()))
    cw.save()


window = tk.Tk()
window.title('RecursiveDirectoryHasher')

# Sizing and position
window.resizable(False, False)

btnStyles = {"bg": "#0071bd", "bd": 0, "activebackground": "#0083da", "height": 2, "fg": "#ffffff", "activeforeground": "#fff"}
tk.Label(text="Select folder").grid(row=0, column=0, padx=(50, 10), pady=(80, 10))

pathInput = tk.Entry(width=50, bd=1)
pathInput.grid(row=0, column=1, columnspan=2, padx=10, pady=(80,10), ipady=5)

tk.Button(text="Select folder", bg="#d1d1d1", bd=0, activebackground="#bebebe", command=selectFolder).grid(row=0, column=3, padx=(10, 50), pady=(80, 10), ipadx=10, ipady=5)
tk.Button(text="Run", **btnStyles, command=run).grid(row=1, column=0, columnspan=4, sticky=N+S+W+E, padx=(50, 50), pady=(10, 80))

window.mainloop()