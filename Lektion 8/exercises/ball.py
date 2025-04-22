"""balls"""
#
# Ball class
# mier/2025-04-04
#
# pylint: disable=too-many-instance-attributes

import random
from defaults import BALL_RADIUS
from defaults import CANVAS_HEIGHT, CANVAS_WIDTH
from defaults import COLOURS
from defaults import DELAY
from defaults import MAX_RADIUS, MIN_RADIUS
from defaults import MAX_SPEED

__all__ = ["Ball"]

class Ball:
    """Ball class"""
    # Class variable to keep count of
    # number of ball objects created.
    number_of_balls = 0
    # Number of clicks counter
    number_of_clicks = 0

    def __init__(self, canvas, counter, colour = None, radius:int = None):
        """constructor"""
        # Increase ball count
        Ball.number_of_balls += 1
        self.canvas = canvas
        # Ball radius
        if radius:
            self.radius = int(radius)
        else:
            self.radius = random.randint(MIN_RADIUS, MAX_RADIUS)
        print(type(self.radius))
        # Number of clicks counter, a tkinter.IntVar, defined in the Widgets
        # class (widgets.py), imported in main.py
        self.counter = counter
        # Ball colour, choosen randomly if not given as an argument
        if colour:
            self.colour = colour
        else:
            self.colour = random.choice(COLOURS)
        # Choose speed randomly
        self.x_speed = random.randint(-MAX_SPEED, MAX_SPEED)
        self.y_speed = random.randint(-MAX_SPEED, MAX_SPEED)
        # Randomly place the ball within the canvas
        self.x = random.randint(self.radius, CANVAS_WIDTH - self.radius)
       self.y = random.randint(self.radius, CANVAS_HEIGHT - self.radius)
        # Create an oval (the ball)
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
        Ball.number_of_clicks += 1
        self.counter.set(Ball.number_of_clicks)
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
                    pass #print("foo")

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


if __name__ == "__main__":
    print(__doc__)
