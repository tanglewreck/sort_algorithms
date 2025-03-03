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


class Root(Tk):
    """Root widget. Inherits Tk."""
    def __init__(self, *args, widget_title = None):
        super().__init__(*args)
        self.widget_title = widget_title
        # self.root_widget = Tk()

    def configure(self, *args):
        """configure the root widget"""
        super().configure(*args)
        self.title(self.widget_title)
        self.geometry(ROOT_GEOMETRY)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class Contents(ttk.Frame):
    """Contents widget. Inherits ttk.Frame."""
    def __init__(self, *args, padding = "100"):
        super().__init__(*args)
        self.padding = padding
        # self.contents_config()

    def configure(self, *args):
        """configure the contents frame"""
        super().configure(*args, padding=self.padding)
        
        # add padding around widgets contained in the contents frame
        for child_widget in self.winfo_children():
            child_widget.grid_configure(padx=10, pady=10)


class Label(ttk.Label):
    def __init__(self, *args, text = ""):
        super().__init__(*args)

    # def 

class Widgets:
    """Widget tree"""
    def __init__(self):
        # create the widget tree
        self.root_widget = Root(widget_title="My Window")
        # self.root_widget = Tk()
        # self.contents = ttk.Frame(self.root_widget)
        self.contents = Contents(self.root_widget, padding="250")
        self.label_one = ttk.Label(self.contents)
        self.label_two = ttk.Label(self.contents)
        self.label_three = ttk.Label(self.contents)
        self.button_quit = ttk.Button(self.contents)
        self.button_print = ttk.Button(self.contents)
        self.text_widget = Text(self.contents)

        # configure widgets
        # self.root_config()
        self.root_widget.configure()
        self.contents.configure()
        # self.contents_config()
        self.labels_config()
        self.print_button_config()
        self.quit_button_config()
        self.text_widget_config()

        # place widgets
        self.do_grid()


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
