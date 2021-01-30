"""
Class wraps for tk widgets

"""

import tkinter as tk


# TODO: передалать сеттер как в ткинтере


class CustomWidget(tk.Widget):
    def __init__(self, *args, **kwargs):
        tk.Widget.__init__(self, master=None, *args, **kwargs)

    def setConfig(self, config: dict):
        self.config(**config['config'])
        self.grid(**config['grid'])
        return self


class Input(CustomWidget):
    def __init__(self, *args, **kwargs):
        CustomWidget.__init__(self, widgetName="entry", *args, **kwargs)

    def makeActive(self):
        self.config(state="normal")

    def makeDisabled(self):
        self.config(state="readonly")

    def clear(self):
        self.delete(0, len(self.get()))

    def setText(self, text: str):
        self.clear()
        self.insert(0, text)


i = Input()


class Label(CustomWidget):
    def __init__(self, *args, **kwargs):
        CustomWidget.__init__(self, widgetName="label", *args, **kwargs)


class Button(CustomWidget):
    def __init__(self, *args, **kwargs):
        CustomWidget.__init__(self, widgetName="button", *args, **kwargs)

    def setConfig(self, config: dict):
        self.config(**config['config'])
        self.grid(**config['grid'])
        return self

    @property
    def onclick(self): pass

    @onclick.setter
    def onclick(self, callback):
        self.config(command=callback)
