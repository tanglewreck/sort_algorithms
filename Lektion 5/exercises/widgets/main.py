"""tkinter exercises"""

import sys
from widgettree import WidgetTree

def main():
    """main()"""
    try:
        widget_tree = WidgetTree()
        widget_tree.mainloop()
    except KeyError as exception:
        print(f"Got a KeyError (somewhere): {repr(exception)} ")


# Run the program
if __name__ == "__main__":
    main()
