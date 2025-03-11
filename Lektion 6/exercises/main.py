"""
    Exercises Lesson 6
    Author: Mikael Eriksson
    Date: 2025-03-11
"""

# pylint: disable=unused-import
# pylint: disable=eval-used

import functools
import exercise_1
import exercise_3

def main():
    """main:"""
    # print(f"{exercise_1.__doc__}")
    try:
        functions = [exercise_1, exercise_3]
        for func in functions:
            func.main()
    except NameError as exception:
        print(repr(exception))
    except OSError as exception:
        print(f"OSError {exception}")


if __name__ == "__main__":
    main()
