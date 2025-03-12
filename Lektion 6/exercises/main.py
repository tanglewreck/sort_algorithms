"""
    Exercises Lesson 6
    Author: Mikael Eriksson
    Date: 2025-03-11
"""

import exercise_1
import exercise_3
import exercise_4
import exercise_5
import exercise_6
import exercise_7
import exercise_8
import exercise_9

def main():
    """main:"""
    try:
        functions = [exercise_1,
                     exercise_3,
                     exercise_4,
                     exercise_5,
                     exercise_6,
                     exercise_7,
                     exercise_8,
                     exercise_9
                     ]
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
