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
import exercise_4

def main():
    """main:"""
    try:
        functions = [exercise_1, exercise_3, exercise_4]
        for func in functions:
            func.main()
    # if function does not exist:
    except NameError as exception:
        print(repr(exception))
    # handle permission error
    except OSError as exception:
        print(f"OSError {exception}")


if __name__ == "__main__":
    main()
