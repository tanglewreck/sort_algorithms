"""tkinter widget tree"""

import sys
import time
from datetime import datetime
from functools import partial
from tkinter import filedialog
from tkinter import N, E, W, S
from tkinter import END
from tkinter import TclError
from widgets import Root, Contents, Label, Button, TextWidget

# pylint: disable=too-many-ancestors
# pylint: disable=too-many-instance-attributes

class WidgetTree:
    """Widget tree class: creates some widgets using custom
       (sub-)classes of tkinter widget classes"""

    def __init__(self):
        # the root widget (custom class)
        self.root_widget = Root()

        # then the contents frame (custom class)
        self.contents = Contents(self.root_widget)

        # then the labels.
        now = datetime(*time.localtime()[0:5])
        (my_date, my_time) = (f"{now.year:04d}-{now.month:02d}-{now.day:02d}",
                              f"{now.hour:02d}:{now.minute:02d}")
        # self.label_date_header = Label(self.contents, text="Date")
        self.label_date = Label(self.contents, text=my_date)
        self.label_time = Label(self.contents, text=my_time)
        self.label_filename = Label(self.contents, text="")

        # then the buttons
        self.button_quit = Button(self.contents, text="Quit")
        self.button_open_file = Button(self.contents, text="Open File")
        # and finaly, the Text widget
        self.text_widget = TextWidget(self.contents)
        self.text_widget.insert("end",
                                "Press the 'Open File' button to "
                                "open and display a file...\n")

        # configure widgets
        self.contents.configure()
        self.open_file_button_config()
        self.quit_button_config()

        # place widgets
        self.do_grid()

        # self.opened_file = None

    def quit_button_config(self):
        """configure the quit button"""
        self.button_quit.config(command=partial(self.root_widget.destroy))

    def open_file_button_config(self):
        """configure the 'press  me' button"""
        # self.button_open_file.config(
        #        command=partial(self.label_filename.config,
        #                        text="'press me' button PRESSED"))
        def openfiledialog():
            # this is rather a mess; just trying stuff out
            try:
                opened_file = filedialog.askopenfilename(initialdir=".")
                if opened_file:
                    with open(opened_file, 'r', encoding="utf8") as file:
                        file_contents = file.read()
                        self.text_widget.delete("1.0", END)
                        self.text_widget.insert(END, file_contents)
                        self.label_filename['text'] = f"{opened_file}"
            except UnicodeDecodeError as exception:
                # If user escapes out of the file dialog, ignore
                # pass
                if __debug__:
                    print(f"Got a UnicodeDecodeError: {exception}",
                          file=sys.stderr)
                    print(f"opened_file: {opened_file}", file=sys.stderr)
                self.text_widget.delete("1.0", END)
                self.text_widget.insert(END, f"{exception}:\n{opened_file}")
            except TypeError as exception:
                # If user escapes out of the file dialog, ignore
                # pass
                print(f"Got a TypeError: {repr(exception)}")
                print(f"opened_file: {opened_file}")
                self.text_widget.delete("1.0", END)
                self.text_widget.insert(END, f"{exception}:\n{opened_file}")
            except PermissionError as exception:
                # Also ignore File Not Found errors
                # (e.g. when trying to open a binary file)
                if __debug__:
                    print(f"Got a PermissionError: {exception}",
                          file=sys.stderr)
                    print(f"opened_file: {opened_file}",
                          file=sys.stderr)
                self.text_widget.delete("1.0", END)
                self.text_widget.insert(END, f"{exception}:\n{opened_file}")
            except FileNotFoundError as exception:
                # Also ignore File Not Found errors
                # (e.g. when trying to open a binary file)
                if __debug__:
                    print(f"Got a FileNotFoundError: {exception}",
                          file=sys.stderr)
                    print(f"opened_file: {opened_file}",
                          file=sys.stderr)
                self.text_widget.delete("1.0", END)
                self.text_widget.insert(END, f"{exception}:\n{opened_file}")
            except OSError as exception:
                if __debug__:
                    print(f"Got an OSError : {exception}",
                          file=sys.stderr)
                    print(f"opened_file: {opened_file}",
                          file=sys.stderr)
                self.text_widget.delete("1.0", END)
                self.text_widget.insert(END, f"{exception}:\n{opened_file}")
            except TclError as exception:
                if __debug__:
                    print(f"Got a TclError: {exception}",
                          file=sys.stderr)
                    print(f"opened_file: {opened_file}",
                          file=sys.stderr)
                self.text_widget.delete("1.0", END)
                self.text_widget.insert(END, f"{exception}:\n{opened_file}")

        self.button_open_file.config(
                command=openfiledialog)

    def do_grid(self):
        """place widgets using grid()"""
        self.contents.grid(column=0, row=0, sticky=(N,E,S,W))
        # self.label_date_header.grid(column=0, row=0, pady=0)
        self.label_date.grid(column=0, row=1, sticky=W)
        self.label_time.grid(column=2, row=1, sticky=E)
        self.label_filename.grid(column=1, row=2, sticky=(E, W))
        self.button_open_file.grid(column=1, row=3, sticky=(E, W))
        self.button_quit.grid(column=1, row=4, sticky=(E, W))
        self.text_widget.grid(column=1, row=1, sticky=(E, W))

    def mainloop(self):
        """execute the root widget mainloop"""
        self.root_widget.mainloop()


# If run from the commandline
if __name__ == "__main__":
    pass
