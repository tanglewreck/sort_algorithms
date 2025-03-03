"""
Använd Tkinter för att skapa ett fönster som du ger titeln "Mitt fönster"
"""

import sys
from functools import partial

from tkinter import ttk
from tkinter import Text
from tkinter import Tk
from tkinter import N, W, S, E

# Root window geometry
R_HEIGHT = 500
R_WIDTH = 800
R_X = 100
R_Y = 0
ROOT_GEOMETRY = f"{R_WIDTH}x{R_HEIGHT}+{R_X}+{R_Y}"


class Widgets:
    """Widget tree"""
    def __init__(self):
        # create the widget tree
        self.root_widget = Tk()
        self.contents = ttk.Frame(self.root_widget)
        self.label_one = ttk.Label(self.contents)
        self.label_two = ttk.Label(self.contents)
        self.label_three = ttk.Label(self.contents)
        self.button_quit = ttk.Button(self.contents)
        self.button_print = ttk.Button(self.contents)
        self.text_widget = Text(self.contents)

        # configure widgets
        self.root_config()
        self.contents_config()
        self.labels_config()
        self.print_button_config()
        self.quit_button_config()
        self.text_widget_config()

        # place widgets
        self.do_grid()


    def root_config(self):
        """configure the root widget"""
        self.root_widget.title("my window")
        self.root_widget.geometry(ROOT_GEOMETRY)
        self.root_widget.columnconfigure(0, weight=1)
        self.root_widget.rowconfigure(0, weight=1)

    def contents_config(self):
        """configure the contents frame"""
        # self.contents.config(padding="3 3 12 12")
        self.contents.config(padding="100 100 100 100")

        # walk through all widgets contained in the contents frame
        # and add padding around them
        for child_widget in self.contents.winfo_children():
            child_widget.grid_configure(padx=10, pady=10)

    def labels_config(self):
        """configure buttons"""
        self.label_one.config(text="label one")
        self.label_two.config(text="label two")
        self.label_three.config(text="label three")

    def quit_button_config(self):
        """configure quit button"""
        quit_func = partial(self.root_widget.destroy)
        self.button_quit.config(text="quit", command=quit_func)

    def print_button_config(self):
        """configure the 'print' button"""
        def print_func():
            self.label_three.config(text="button pressed")
        # print_func = partial(print, "button pressed", file=sys.stderr)
        self.button_print.config(text="press me", command=print_func)

    def text_widget_config(self):
        """configure the text widget"""
        self.text_widget.configure(width=20, height=5)

    def do_grid(self):
        """place widgets using grid()"""
        self.contents.grid(column=0, row=0, sticky=(N,E,S,W))
        self.label_one.grid(column=0, row=0, sticky=W)
        self.label_two.grid(column=2, row=0, sticky=E)
        self.label_three.grid(column=1, row=1, sticky=(E, W))
        self.button_print.grid(column=1, row=2, sticky=(E, W))
        self.button_quit.grid(column=1, row=3, sticky=(E, W))
        self.text_widget.grid(column=1, row=0, sticky=(E, W))

    def do_mainloop(self):
        """execute the root widget mainloop"""
        self.root_widget.mainloop()
