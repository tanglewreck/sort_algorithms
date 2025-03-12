"""= = = = = =
Exercise 6
= = = = = = """
# Skriv ut den rad som har en 4 i sig

import re
from defaults import DEFAULTS

__all__ = ['main']

def main():
    """main() of exercise 1"""
    print(__doc__)
    file_name = DEFAULTS['files']['fileName']
    regexp = r".*4"
    try:
        with open(file_name, 'r', encoding="utf8") as file:
            rows = file.readlines()
            for (row_number, row) in enumerate(rows):
                try:
                    if row.index("4"):
                        print(f"found '4' on row {row_number}: {row.strip()}")
                    if re.match(regexp, row):
                        print(f"found regexp ('{regexp}') on row {row_number}: "
                              f"{row.strip()}")
                except ValueError:
                    # print(f"{exception}")
                    pass
            # print(f"Successfully wrote to {file_name}")
        #utils.print_file_contents(file_name)

    except OSError as exception:
        print(f"{exception}")
        raise


if __name__ == "__main__":
    print(__doc__)
    main()
