"""
Använd Tkinter för att skapa ett fönster som du ger titeln "Mitt fönster"
"""


from tkinter import Tk, Frame
from tkinter import Button, Label
# from tkinter import N, W, S, E

# Root window geometry
R_HEIGHT = 500
R_WIDTH = 800
R_X = 100
R_Y = 0
ROOT_GEOMETRY = f"{R_WIDTH}x{R_HEIGHT}+{R_X}+{R_Y}"


root_widget = Tk()
root_widget.title("my window")
root_widget.geometry(ROOT_GEOMETRY)

contents = Frame(root_widget)
button_one = Button(contents, text="foo button")
label_one = Label(contents, text="foo label")

contents.grid()
button_one.grid()
label_one.grid()

root_widget.mainloop()
