"""Default values for balls simulation"""
__all__ = ["BALL_RADIUS",
           "CANVAS_HEIGHT",
           "CANVAS_WIDTH",
           "COLOURS",
           "DELAY",
           "MAX_SPEED",
           "MIN_SPEED"]

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
# Max and min ball radius
MAX_RADIUS = 30
MIN_RADIUS = 10
# Number of balls to create
NUMBER_OF_BALLS = 5
