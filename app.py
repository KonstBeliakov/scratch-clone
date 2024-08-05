import tkinter as tk
from tkinter import ttk

from frames import *
from run_script import start_script


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_header = tk.Label(self, text='Setup script')
        self.setup_header.pack()

        self.text_setup = tk.Text(self, height=5, width=30)
        self.text_setup.pack()

        self.main_loop_header = tk.Label(self, text='Main loop script')
        self.main_loop_header.pack()

        self.text_main_loop = tk.Text(self, height=5, width=30)
        self.text_main_loop.pack()

        button = tk.Button(self, text="Run script",
                           command=lambda: start_script(self.text_setup.get("1.0", "end-1c"),
                                                        self.text_main_loop.get("1.0", "end-1c")))
        button.pack()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        self.python_frame = PythonFrame(self)
        self.notebook.add(self.python_frame, text='Basics')

        self.motion_frame = MotionFrame(self)
        self.notebook.add(self.motion_frame, text='Motion')

        self.look_frame = LookFrame(self)
        self.notebook.add(self.look_frame, text='Look')

        self.sensing_frame = SensingFrame(self)
        self.notebook.add(self.sensing_frame, text='Sense')

    def copy_code(self, frame, line_number, to_setup=False):
        if not to_setup:
            self.text_main_loop.insert(tk.END, '\n' + frame.labels[line_number]['text'])
        else:
            self.text_setup.insert(tk.END, '\n' + frame.labels[line_number]['text'])

