"""exercise lesson 8"""

import random
from tkinter import Button
from tkinter import Canvas
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk


# Initialise list (of balls)
BALLS = []

# The size of the Canvas widget implicitly determines
# the size of the root widget:
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
# Selection of ball colours
COLOURS = ["red",
           "green",
           "blue",
           "yellow"]
# delay in ms until a ball is moved (again)
DELAY = 50
# Max and min speed in both x and y directions
MAX_SPEED = 3
MIN_SPEED = 1
# Number of balls to create
NUMBER_OF_BALLS = 5



class Ball:
    """Ball class"""
    # Class variable to keep count of
    # number of ball objects created.
    number_of_balls = 0
    # Number of clicks counter
    number_of_clicks = 0

    def __init__(self, canvas, colour, radius):
        """constructor"""
        # Increase ball count
        # Ball.number_of_balls += 1
        self.__class__.number_of_balls += 1
        self.canvas = canvas
        self.radius = radius
        self.colour = colour
        # Choose speed randomly
        self.x_speed = random.randint(MIN_SPEED, MAX_SPEED)
        self.y_speed = random.randint(MIN_SPEED, MAX_SPEED)
        # Randomly place the ball within the canvas
        x = random.randint(self.radius, CANVAS_WIDTH - self.radius)
        y = random.randint(self.radius, CANVAS_HEIGHT - self.radius)
        # Create an oval
        self.ball = self.canvas.create_oval(x - self.radius,
                                            y - self.radius,
                                            x + self.radius,
                                            y + self.radius,
                                            fill=self.colour)
        # Bind mousebutton 1 to the colour changing method
        self.canvas.tag_bind(self.ball, '<Button-1>', self.change_colour)

    def change_colour(self, _ = None):
        """Change ball colour, randomly"""
        # Update number of clicks counter
        self.__class__.number_of_clicks += 1
        print(self.__class__.number_of_clicks)
        # If the ball is blue, reverse
        if self.colour == "blue":
            self.reverse()

        # If the ball is yellow, make it green; if it's
        # green, delete it; else randomly choose a colour
        #
        if self.colour == "yellow":
            new_colour = "green"
        # If the ball is green and there's more than
        # one ball still left, delete the ball (i.e.
        # delete the canvas oval that is the visual 
        # representation of the ball; the ball object 
        # is not deleted).
        elif self.colour == "green" and \
             self.__class__.number_of_balls > 1:
            # Make pylint not complain about 'Possibly
            # using varable "new_colour" before assignment' by assigning some
            # arbitrary value... (not really necessary, code wise):
            new_colour = None
            # Delete the ball/oval
            self.canvas.delete(self.ball)
            # Decrease ball count
            self.__class__.number_of_balls -= 1
        else:
            new_colour = random.choice(COLOURS)
        self.canvas.itemconfig(self.ball, fill=new_colour)
        self.colour = new_colour

        # Set a timer so the ball keeps changing colour
        # self.canvas.after(1000, self.change_colour, None)

    def reverse(self, _ = None):
        """Change/reverse direction"""
        self.x_speed *= -1
        self.y_speed *= -1

    def move(self):
        """Move the ball"""
        # Move the ball
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        # Get new coordinates (after the ball has moved)
        try:
            x1, y1, x2, y2 = self.canvas.coords(self.ball)
            # If outside the canvas, reverse direction
            if x1 <= 0 or x2 >= CANVAS_WIDTH:
                self.x_speed *= -1
            if y1 <= 0 or y2 >= CANVAS_HEIGHT:
                self.y_speed *= -1
            # Set the ball moving again after a delay
            self.canvas.after(DELAY, self.move)
        except ValueError:
            # If the ball/oval has been deleted, a ValueError
            # is raised the next time self.move() is called, so
            # we catch these errors and ignore them:
            pass


def main():
    """main()"""

    # root widget
    root = Tk()
    root.title("balls")

    # Create a canvas where the balls can move around
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()


    # Add balls to the list
    ball_radius = 20
    # NB: This is a logical error in the
    # original code (the colour should be "blue")
    # ball_colour = "#1122FF"
    for _ in range(NUMBER_OF_BALLS):
        ball_colour = random.choice(COLOURS)
        BALLS.append(Ball(canvas, ball_colour, ball_radius))


    # Set the balls in motion
    for ball in BALLS:
        ball.move()

    # Add a counter label
    counter_var = StringVar()
    counter_var.set(str(Ball.number_of_clicks))
    counter_label = Label(root, textvariable=counter_var)
    counter_label.after(1000, 
                        )
    counter_label.pack()

    # Add a Quit-button
    quit_button = Button(root,
                         text="Quit",
                         command=quit)
    quit_button.pack()
    # Execute the mainloop
    root.mainloop()

if __name__ == "__main__":
    main()
