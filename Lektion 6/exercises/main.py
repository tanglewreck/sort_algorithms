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

###7import exercise_1
###7import exercise_3
###7import exercise_4
###7import exercise_5
###7import exercise_6
###7import exercise_7
###7import exercise_8
###7import exercise_9
###def main():
###    """main:"""
###    try:
###        functions = [exercise_1,
###                     exercise_3,
###                     exercise_4,
###                     exercise_5,
###                     exercise_6,
###                     exercise_7,
###                     exercise_8,
###                     exercise_9
###                     ]
###        for func in functions:
###            func.main()
###    # if function does not exist:
###    except NameError as exception:
###        print(repr(exception))
###    # handle permission error
###    except OSError as exception:
###        print(f"OSError {exception}")


if __name__ == "__main__":
    main()
