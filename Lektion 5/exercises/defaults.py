"""Default values for widgets"""

import json

__all__ = ["ROOT_GEOMETRY",
           "DEFAULTS"]


# Root window geometry
R_HEIGHT = 500
R_WIDTH = 800
R_X = 100
R_Y = 20
ROOT_GEOMETRY = f"{R_WIDTH}x{R_HEIGHT}+{R_X}+{R_Y}"
DEFAULTS = {
        "Button":   {"padding": 10, "width": 20},
        "Label":    {"anchor": 'center', "border": 5,
                     "borderwidth": 2, "justify": 'right',
                     "padding": "10 10 10 10", "relief": "raised",
                     "underline": 2, "width": 10},
        "Contents": {"padding": 100},
        "Text":     {"background": "#aaaaaa", "foreground": "#002055",
                     "height": 8, "width": 30}
}
def save_json():
    """Save defaults to file in json format"""
    # defaults_json = json.dumps(DEFAULTS)
    try:
        with open("defaults.json", "w", encoding="utf8") as file_descriptor:
            json.dump(DEFAULTS, file_descriptor)
    except OSError as exception:
        print(f"Error: {exception}")

if __name__ == "__main__":
    save_json()
