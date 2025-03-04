"""tkinter widget tree"""

from functools import partial
from tkinter import Text
from tkinter import N, E, W, S
from tkinter.ttk import Style
from widgets import Root, Contents, Label, Button, TextWidget
from widgets import ROOT_GEOMETRY


class WidgetTree:
    """Widget tree class: creates some widgets using custom
       (sub-)classes of tkinter widget classes"""

    def __init__(self):
        # the root widget (custom class)
        self.root_widget = Root(title="My Window", geometry=ROOT_GEOMETRY)
        # then the contents frame (custom class)
        self.contents = Contents(self.root_widget, padding="200")
        # then the labels
        self.label_one = Label(self.contents, text="label one")
        self.label_two = Label(self.contents, text="label two") 
        self.label_three = Label(self.contents, text="label three")
        # then the buttons
        self.button_quit = Button(self.contents, text="Quit")
        self.button_print = Button(self.contents, text="press ME")
        # and finaly, the Text widget
        self.text_widget = TextWidget(self.contents)

        # configure widgets
        self.contents.configure()
        self.print_button_config()
        self.quit_button_config()

        # place widgets
        self.do_grid()

    def quit_button_config(self):
        """configure the quit button"""
        self.button_quit.config(command=partial(self.root_widget.destroy))

    def print_button_config(self):
        """configure the 'press  me' button"""
        self.button_print.config(
                command=partial(self.label_three.config,
                                text="'press me' button PRESSED"))

    def do_grid(self):
        """place widgets using grid()"""
        self.contents.grid(column=0, row=0, sticky=(N,E,S,W))
        self.label_one.grid(column=0, row=0, sticky=W)
        self.label_two.grid(column=2, row=0, sticky=E)
        self.label_three.grid(column=1, row=1, sticky=(E, W))
        self.button_print.grid(column=1, row=2, sticky=(E, W))
        self.button_quit.grid(column=1, row=3, sticky=(E, W))
        self.text_widget.grid(column=1, row=0, sticky=(E, W))

    def mainloop(self):
        """execute the root widget mainloop"""
        self.root_widget.mainloop()
