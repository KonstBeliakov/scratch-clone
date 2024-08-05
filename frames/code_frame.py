from tkinter import *
from tkinter import ttk


class CodeFrame(ttk.Frame):
    def __init__(self, app, values):
        super().__init__()
        self.app = app
        self.values = values

        self.labels = [Label(self, text=value) for value in values]
        for i, label in enumerate(self.labels):
            label.grid(row=i, column=0, sticky=W)

        self.buttons = [Button(self, text='Copy') for i in range(len(values))]
        for i in range(len(self.buttons)):
            self.bind_function(i)
        for i, button in enumerate(self.buttons):
            button.grid(row=i, column=1)

    def bind_function(self, i):
        self.buttons[i].config(command=lambda: self.app.copy_code(self, i))
