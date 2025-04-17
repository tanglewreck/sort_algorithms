"""Exercises lesson 8"""

import random
import sys
# from defaults import BALL_RADIUS
from defaults import CANVAS_HEIGHT, CANVAS_WIDTH
from defaults import COLOURS
from defaults import NUMBER_OF_BALLS
from ball import Ball
from widgets import Widgets
# from utils import get_defaults


def main():
    """main()"""

    # Get defaults
    # get_defaults()

    # Get number of balls to create
    try:
        number_of_balls = abs(int(sys.argv[1]))
    except IndexError:
        number_of_balls = NUMBER_OF_BALLS
    except (ValueError, NameError) as exception:
        print(repr(exception))
        raise SystemExit(1) from exception

    # Create an orange oval in the middle of the canvas
    widgets = Widgets(timeout=10000)
    r = 30
    x, y = (CANVAS_WIDTH + r) / 2, (CANVAS_HEIGHT + r) / 2
    widgets.canvas.create_oval(x - r, y - 2 * r, x + r, y + 2 * r, fill="orange")
    widgets.canvas.create_oval(x - 4 * r, y - r, x + 4 * r, y + r, fill="orange")
    # Add balls to the list
    # NB: This is a logical error in the
    # original code (the colour should be "blue")
    # ball_colour = "#1122FF"
    balls = []
    for _ in range(number_of_balls):
        ball_colour = random.choice(COLOURS)
        balls.append(Ball(widgets.canvas,
                          widgets.counter_var,
                          ball_colour
                          )
                     )


    # Set the balls in motion
    for ball in balls:
        ball.move(balls)

    # Execute the mainloop
    widgets.root.mainloop()

if __name__ == "__main__":
    main()
