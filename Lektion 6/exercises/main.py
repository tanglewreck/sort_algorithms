"""
    Exercises Lesson 6
    Author: Mikael Eriksson
    Date: 2025-03-11
"""

import functools
import exercise_1
import exercise_3

def main():
    """main:"""
    # print(f"{exercise_1.__doc__}")
    try:
        #func()
        for k in [1, 3]:
            # func = functools.partial(f"exercise_{k}")
            func = f"exercise_{k}.main()"
            eval(func)
    except NameError as exception:
        print(repr(expression))
    except OSError as exception:
        print("OSError in exercise 1")


if __name__ == "__main__":
    main()
