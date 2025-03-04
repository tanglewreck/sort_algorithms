"""
Använd Tkinter för att skapa ett fönster som du ger titeln "Mitt fönster"
"""

from tkinter import ttk
from tkinter import Tk

# Root window geometry
R_HEIGHT = 500
R_WIDTH = 800
R_X = 100
R_Y = 20
ROOT_GEOMETRY = f"{R_WIDTH}x{R_HEIGHT}+{R_X}+{R_Y}"


class Root(Tk):
    """Root widget. Inherits Tk."""
    # def __init__(self, *args, title = None):
    def __init__(self, *args, title = None, geometry = ROOT_GEOMETRY, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget_title = title
        self.title(title)
        self.geometry(geometry)
        self.configure()

    def configure(self, *args, **kwargs):
        """configure the root widget"""
        super().configure(*args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class Contents(ttk.Frame):
    """ttk.Frame subclass"""
    def __init__(self, *args,
                 padding = 100,
                 padding_children = 10,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = padding
        self.padding_children = padding_children

    def configure(self, *args, **kwargs):
        """configure the contents frame"""
        super().configure(*args, **kwargs, padding=self.padding)

        # add padding around widgets contained in the contents frame
        for child_widget in self.winfo_children():
            child_widget.grid_configure(padx=self.padding_children,
                                        pady=self.padding_children)


class Label(ttk.Label):
    """self-configurating ttk.Label subclass"""
    def __init__(self, *args,
                 text = None,
                 anchor = 'center',
                 background = "#000000",
                 foreground = "#00f0ff",
                 border = 5,
                 justify = 'right',
                 padding = "10 10 10 10",
                 underline=2,
                 width=10,
                 **kwargs):
        # Call parent-class initialiser
        super().__init__(*args, **kwargs)

        # Custom-configure the widget using the explicitly
        # defined keyword arguments to the constructor.
        self.configure(background=background,
                       foreground=foreground,
                       anchor=anchor,
                       border=border,
                       justify=justify,
                       padding=padding,
                       text=text,
                       underline=underline,
                       width=width)

    def configure(self, *args, **kwargs):
        """Configure the label, overriding
        tkinter.Label.configure"""
        super().configure(*args, **kwargs)


class Button(ttk.Button):
    """Custom Button class; inherits ttk.Button"""
    def __init__(self, *args, text = None, **kwargs):
        super().__init__(*args, text=text, **kwargs)
