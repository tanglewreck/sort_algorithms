"""
Widget classes
"""

from tkinter import ttk
from tkinter import Tk
from tkinter import Text
from tkinter.ttk import Style
from defaults import DEFAULTS

# pylint: disable=too-many-ancestors

class Root(Tk):
    """Root widget. Inherits Tk."""
    def __init__(self, *args, title = DEFAULTS["Root"]["Title"],
                 geometry = DEFAULTS["Root"]["Geometry"], **kwargs):
        super().__init__(*args, **kwargs)
        if title:
            self.title(title)
        if geometry:
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
                 padding_children = 10,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.padding_children = padding_children

        # ttk uses styles and themes use themes with different
        # default themes for different platforms, e.g. on MacOS
        # the default theme is 'aqua', where for some obscure reason
        # the background colour of buttons can't be changed, so we
        # set the default theme explicitly so button backgrounds can
        # be set.
        style = Style()
        style.theme_use('default')

        # Define and use a style for our contents frame
        style.configure("Contents.TFrame", foreground="orange", background="#202020")
        self['style'] = 'Contents.TFrame'

    def configure(self, *args, padx = 10, pady = 10, **kwargs):
        """configure the contents frame"""
        # Update kwargs with keyword arguments (from the DEFAULTS dictionary)
        kwargs.update(DEFAULTS["Contents"])
        super().configure(*args, **kwargs)

        # add padding around widgets contained in the contents frame
        for child_widget in self.winfo_children():
            child_widget.grid_configure(padx=padx,
                                        pady=pady)


class Label(ttk.Label):
    """self-configurating ttk.Label subclass"""
    def __init__(self, *args,
                 text = None,
                 **kwargs):
        # Update kwargs with keyword arguments (from the DEFAULTS dictionary)
        kwargs.update(DEFAULTS["Label"])
        # Call parent-class initialiser
        super().__init__(*args, **kwargs)

        # Custom-configure the widget using the explicitly
        # defined keyword arguments to the constructor.
        self.configure(text=text) #, **kwargs)

        # Define and use a style for objects of this class
        label_style = Style()
        label_style.configure("Labels.TLabel",
                              foreground="#505050",
                              background="#ffff50")
        self["style"] = "Labels.TLabel"

    def configure(self, *args, **kwargs):
        """Configure label"""
        super().configure(*args, **kwargs)


class Button(ttk.Button):
    """Custom Button class; inherits ttk.Button"""
    # def __init__(self, *args, text = None, **kwargs):
    def __init__(self, *args, **kwargs):
        # Update kwargs with keyword arguments (from the DEFAULTS dictionary)
        # and call the superclass initialiser
        kwargs.update(DEFAULTS["Button"])
        super().__init__(*args, **kwargs)

        # Define and use a ttk style for buttons
        button_style = Style()
        button_style.theme_use('default')
        button_style.configure('White.TButton', foreground="#101010", background="#55aaff")
        self['style'] = 'White.TButton'


class TextWidget(Text):
    """Custom TextWidget class; inherits tkinter.Text"""
    def __init__(self, *args, **kwargs):
        # Update kwargs with keyword arguments (from the DEFAULTS dictionary)
        kwargs.update(DEFAULTS["Text"])
        super().__init__(*args, **kwargs)


# If run from the commandline
if __name__ == "__main__":
    pass
