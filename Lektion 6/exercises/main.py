"""
    Exercises Lesson 6
    Author: Mikael Eriksson
    Date: 2025-03-11
"""


from widgettree import WidgetTree

def main():
    """main()"""
    try:
        widget_tree = WidgetTree()
        widget_tree.mainloop()
    except KeyError as exception:
        print(f"Got a KeyError (somewhere): {repr(exception)} ")


if __name__ == "__main__":
    main()
