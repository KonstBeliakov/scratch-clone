import tkinter as tk
from run_script import run_script


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_header = tk.Label(self, text='Setup script')
        self.setup_header.pack()

        text_setup = tk.Text(self, height=5, width=30)
        text_setup.pack()

        self.main_loop_header = tk.Label(self, text='Main loop script')
        self.main_loop_header.pack()

        text_main_loop = tk.Text(self, height=5, width=30)
        text_main_loop.pack()

        button = tk.Button(self, text="Run script",
                           command=lambda: run_script(text_setup.get("1.0", "end-1c"),
                                                      text_main_loop.get("1.0", "end-1c")))
        button.pack()
