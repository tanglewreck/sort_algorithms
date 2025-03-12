"""= = = = = =
Exercise 4
= = = = = = """

import subprocess
import utils
from defaults import DEFAULTS

__all__ = ['main']

def main():
    """main of exercise 4"""
    def copy_file_1(file: str = None) -> str:
        file_copy = f"{file}.copy"
        cp = ["cp", file, file_copy]
        try:
            res = subprocess.
    print(__doc__)
    file_name = DEFAULTS['files']['fileName1']
    file_copy = DEFAULTS['files']['fileName2']
    try:
        with open(file_name, 'r', encoding="utf8") as fd_one:
            with open(file_copy, 'w', encoding="utf8") as fd_two:
                file_data = fd_one.read()
                fd_two.write(file_data)
        print(f"Successfully copied {file_name} to {file_copy}")
        #sha256_sum = "/usr/bin/sha256sum"
        #subprocess
        utils.print_file_contents(file_copy)
    except FileNotFoundError as exception:
        print(f"{exception}")
    except OSError as exception:
        print(f"{exception}")
        raise

if __name__ == "__main__":
    print(__doc__)
    main()
