"""
Class wraps for tk widgets

"""

import tkinter as tk

# Trait configurator wich contains setconfig method


class TWidgetConfigurator():
    def set_config(self, config: dict):
        self.config(**config['config'])
        self.grid(**config['grid'])
        return self


class Input(tk.Entry, TWidgetConfigurator):
    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, args, **kwargs)

    def makeActive(self):
        self.config(state="normal")

    def makeDisabled(self):
        self.config(state="readonly")

    def clear(self):
        self.delete(0, len(self.get()))

    def setText(self, text: str):
        self.clear()
        self.insert(0, text)


class Label(tk.Label, TWidgetConfigurator):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)


class Button(tk.Button, TWidgetConfigurator):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.bind('<Enter>', self.onhover)
        self.bind('<Leave>', self.onleave)

    @ property
    def onclick(self): pass

    @ onclick.setter
    def onclick(self, callback):
        self.config(command=callback)

    def onhover(self, event):
        # self.config(bg="#00538a")
        pass

    def onleave(self, event):
        self.config(bg=self['bg'])


class CheckButton(tk.Checkbutton, TWidgetConfigurator):
    def __init__(self, *args, **kwargs):
        tk.Checkbutton.__init__(self, *args, **kwargs)
