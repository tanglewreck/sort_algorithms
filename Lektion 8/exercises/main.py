"""exercise lesson 8"""

import random
import sys
from tkinter import Button
from tkinter import Canvas
from tkinter import Label
from tkinter import IntVar
from tkinter import Tk
from tkinter import W, E

# pylint: disable=too-many-instance-attributes

BALL_RADIUS = 20
# The size of the Canvas widget implicitly determines
# the size of the root widget:
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800
# Selection of ball colours
COLOURS = ["red",
           "green",
           "blue",
           "yellow"]
# delay in ms until a ball is moved (again)
DELAY = 50
# Max and min speed in both x and y directions
MAX_SPEED = 7
MIN_SPEED = 1
# Number of balls to create
try:
    NUMBER_OF_BALLS = abs(int(sys.argv[1]))
except IndexError:
    NUMBER_OF_BALLS = 15
except (ValueError, NameError) as exception:
    print(repr(exception))
    raise SystemExit(1) from exception


class Ball:
    """Ball class"""
    # Class variable to keep count of
    # number of ball objects created.
    number_of_balls = 0
    # Number of clicks counter
    number_of_clicks = 0

    def __init__(self, canvas, colour, radius, counter):
        """constructor"""
        # Increase ball count
        Ball.number_of_balls += 1
        self.canvas = canvas
        self.radius = radius
        self.colour = colour
        self.counter = counter
        # Choose speed randomly
        self.x_speed = random.randint(-MAX_SPEED, MAX_SPEED)
        self.y_speed = random.randint(-MAX_SPEED, MAX_SPEED)
        # Randomly place the ball within the canvas
        self.x = random.randint(self.radius, CANVAS_WIDTH - self.radius)
        self.y = random.randint(self.radius, CANVAS_HEIGHT - self.radius)
        # Create an oval
        self.ball = self.canvas.create_oval(self.x - self.radius,
                                            self.y - self.radius,
                                            self.x + self.radius,
                                            self.y + self.radius,
                                            fill=self.colour)
        # Bind mousebutton 1 to the colour changing method
        self.canvas.tag_bind(self.ball, '<Button-1>', self.do_button_1_click)

    def do_button_1_click(self, _):
        """Handle button-1 click"""
        # Update number of clicks counter
        #Ball.number_of_clicks += 1
        self.counter.set(Ball.number_of_clicks + 1)
        # If the ball is blue, reverse
        if self.colour == "blue":
            self.reverse()
        # Change ball colour
        self.change_colour()

    def change_colour(self, _ = None):
        """Change ball colour, randomly"""
        # If the ball is yellow, make it green; if it's
        # green, delete it; else randomly choose a colour
        #
        if self.colour == "yellow":
            new_colour = "green"
        elif self.colour == "green" and \
             Ball.number_of_balls > 1:
            # If the ball is green and there's more than
            # one ball still left, delete the ball (i.e.
            # delete the canvas oval that is the visual
            # representation of the ball; the ball object
            # is not deleted).

            # Decrease ball count
            Ball.number_of_balls -= 1
            # Make pylint not complain about 'Possibly
            # using varable "new_colour" before assignment' by assigning some
            # arbitrary value... (not really necessary, code wise):
            new_colour = None
            # Delete the ball/oval.
            # NB the Ball object is not deleted.
            self.canvas.delete(self.ball)
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

    def move(self, balls):
        """Move the ball"""

        def do_collisions(balls):
            """Handle ball collisions"""
            for ball in balls:
                if ball.x + BALL_RADIUS > self.x - BALL_RADIUS:
                    print("foo")

        # Move the ball
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        # Get new coordinates (after the ball has moved)
        try:
            x1, y1, x2, y2 = self.canvas.coords(self.ball)
            # If outside the canvas, reverse direction
            dr = 0.05 * BALL_RADIUS
            if x1 <= 0:
                self.x_speed *= -1
                while x1 <= 0:
                    self.canvas.move(self.ball, dr, 0)
                    (x1, y1, x2, y2) = self.canvas.coords(self.ball)
            elif x2 >= CANVAS_WIDTH:
                self.x_speed *= -1
                while x2 >= CANVAS_WIDTH:
                    self.canvas.move(self.ball, -dr, 0)
                    (x1, y1, x2, y2) = self.canvas.coords(self.ball)
            if y1 <= 0:
                self.y_speed *= -1
                while y1 <= 0:
                    self.canvas.move(self.ball, 0, dr)
                    (x1, y1, x2, y2) = self.canvas.coords(self.ball)
                self.canvas.move(self.ball, 0, BALL_RADIUS)
            elif y2 >= CANVAS_HEIGHT:
                self.y_speed *= -1
                while y1 >= CANVAS_HEIGHT:
                    self.canvas.move(self.ball, 0, -dr)
                    (x1, y1, x2, y2) = self.canvas.coords(self.ball)
                self.canvas.move(self.ball, 0, -BALL_RADIUS)
            # Set the ball moving again after a delay
            self.canvas.after(DELAY, self.move, balls)
            do_collisions(balls)
        except ValueError:
            # If the ball/oval has been deleted, a ValueError
            # is raised the next time self.move() is called, so
            # we catch these errors and ignore them:
            pass


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


def main():
    """main()"""

    widgets = Widgets(timeout=10000)
    r = 30
    x, y = 0, 100
    widgets.canvas.create_oval(x - r,
                                            y - r,
                                            x + r,
                                            y + r,
                                            fill="orange")
    # Add balls to the list
    # NB: This is a logical error in the
    # original code (the colour should be "blue")
    # ball_colour = "#1122FF"
    balls = []
    for _ in range(NUMBER_OF_BALLS):
        ball_colour = random.choice(COLOURS)
        balls.append(Ball(widgets.canvas,
                          ball_colour,
                          BALL_RADIUS,
                          widgets.counter_var))


    # Set the balls in motion
    for ball in balls:
        ball.move(balls)

    # Execute the mainloop
    widgets.root.mainloop()

if __name__ == "__main__":
    main()
