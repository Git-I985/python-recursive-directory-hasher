import tkinter as tk

class Input(tk.Entry):
    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, *args, **kwargs)

    def makeActive(self):
        self.config(state="normal")
    
    def makeDisabled(self):
        self.config(state="readonly")

    def clear(self):
        self.delete(0, len(self.get()))

    def setText(self, text: str):
        self.clear()
        self.insert(0, text)

    def setConfig(self, config: dict):
        self.config(**config['config'])
        self.grid(**config['grid'])

class Label(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)

    def setConfig(self, config: dict):
        self.config(**config['config'])
        self.grid(**config['grid'])


class Button(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)

    def setConfig(self, config: dict):
        self.config(**config['config'])
        self.grid(**config['grid'])