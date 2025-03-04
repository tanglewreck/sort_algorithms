"""tkinter widget tree"""

from functools import partial
from tkinter import Text
from tkinter import N, E, W, S
from widgets import Root, Contents, Label, Button
from widgets import ROOT_GEOMETRY


class WidgetTree:
    """Widget tree. Uses custom classes:
       Root, Contents, Label, Button"""
    def __init__(self):
        # create the widget tree;
        # first the root widget (custom class)
        self.root_widget = Root(title="My Window", geometry=ROOT_GEOMETRY)
        # then the contents frame (custom class)
        self.contents = Contents(self.root_widget, padding="200")
        # then the labels
        self.label_one = Label(self.contents, text="label one", borderwidth=20)
        self.label_two = Label(self.contents, text="label tw0",
                               borderwidth=20, relief="raised")
        self.label_three = Label(self.contents, text="label thr33")
        # then the buttons
        self.button_quit = Button(self.contents, text="Quuuit", width=20)
        self.button_print = Button(self.contents, text="press ME")
        # and finaly, the Text widget
        self.text_widget = Text(self.contents)

        # configure widgets
        self.contents.configure()
        self.print_button_config()
        self.quit_button_config()
        self.text_widget_config()

        # place widgets
        self.do_grid()


    def quit_button_config(self):
        """configure quit button"""
        self.button_quit.config(command=partial(self.root_widget.destroy))

    def print_button_config(self):
        """configure the 'print' button"""
        def print_func(label):
            label.config(text="button pressed")
        self.button_print.config(
                command=partial(print_func, self.label_three))
        self.button_print.config(takefocus=1,
                                 state="enabled",
                                 underline=3)

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

    def mainloop(self):
        """execute the root widget mainloop"""
        self.root_widget.mainloop()
