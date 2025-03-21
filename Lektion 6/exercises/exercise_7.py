"""= = = = = =
Exercise 7
= = = = = = """
# Öppna din fil "test.txt" och räkna ut hur många rader som finns i din fil
# med en loop.

from defaults import DEFAULTS

__all__ = ['exercise_7_main']

def exercise_7_main():
    """main() of exercise 1"""
    print(__doc__)
    file_name = DEFAULTS['files']['fileName']
    try:
        with open(file_name, 'r', encoding="utf8") as file:
            rows = file.readlines()
            print(f"{file_name} contains {len(rows)} rows")
            file.seek(0)
            no_lines = 0
            while file.readline():
                no_lines += 1
            print(f"number of lines (loop-count): {no_lines}")

    except OSError as exception:
        print(f"{exception}")
        raise


if __name__ == "__main__":
    exercise_7_main()
