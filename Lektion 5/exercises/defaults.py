"""Default values for widgets"""

__all__ = ["ROOT_GEOMETRY",
           "DEFAULTS_BUTTON",
           "DEFAULTS_CONTENTS",
           "DEFAULTS_LABEL",
           "DEFAULTS_TEXT"]


# Root window geometry
R_HEIGHT = 500
R_WIDTH = 800
R_X = 100
R_Y = 20
ROOT_GEOMETRY = f"{R_WIDTH}x{R_HEIGHT}+{R_X}+{R_Y}"
DEFAULTS_BUTTON = {
    "padding": 10,
    "width": 20
}

DEFAULTS_LABEL = {
    "anchor": 'center',
    "border": 5,
    "borderwidth": 2,
    "justify": 'right',
    "padding": "10 10 10 10",
    "relief": "raised", 
    "underline": 2,
    "width": 10
}

DEFAULTS_CONTENTS = {
    "padding": 100
}

DEFAULTS_TEXT = {
    "background": "#aaaaaa",
    "foreground": "#002055",
    "height": 8,
    "width": 30
}
