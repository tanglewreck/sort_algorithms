"""Widget tree"""


from tkinter import Button, Canvas, Label
from tkinter import IntVar
from tkinter import Tk
from tkinter import W, E
from defaults import CANVAS_HEIGHT, CANVAS_WIDTH

class Widgets:
    """Widgets"""
    def __init__(self, timeout):
        # root widget
        self.root = Tk()
        self.root.title("balls")
        self.root.after(timeout, self.root.destroy)
        # self.root.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT + 50}+100+100")

        # Create a canvas where the balls can move around
        self.canvas = Canvas(self.root,
                             width=CANVAS_WIDTH,
                             height=CANVAS_HEIGHT,
                             bg="white")
        self.canvas.grid(row=0, column=0,
                         columnspan=3,
                             sticky=(W,E))

        # Add a counter label
        self.counter_var = IntVar()
        Label(self.root, text="Clicks").grid(row=1,
                                             column=1,
                                             sticky=(W,E))
        counter_label = Label(self.root)
        counter_label.configure(text="Clicks:")
        counter_label.configure(textvariable=self.counter_var)
        counter_label.grid(row=2, column=1, sticky=(W,E))

        # Add a Quit-button
        quit_button = Button(self.root,
                             text="Quit",
                             command=quit)
                             # width=50)
        quit_button.grid(row=3, column=1, sticky=(W, E))


    def balls(self):
        """create balls"""
    def __repr__(self):
        """__repr__"""
        return str(self.root)

    def __str__(self):
        """__str__"""
        return str(self.root)
