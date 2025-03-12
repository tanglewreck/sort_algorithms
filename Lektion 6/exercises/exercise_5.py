"""= = = = = =
Exercise 5
= = = = = = """
# Skriv in 5 rader i "test.txt". Rad1, Rad2, Rad3, Rad4 och Rad5.

import utils
from defaults import DEFAULTS

__all__ = ['main']

def main():
    """main() of exercise 1"""
    print(__doc__)
    file_name = DEFAULTS['files']['fileName']
    text = DEFAULTS['texts']['text2']
    try:
        with open(file_name, 'w', encoding="utf8") as file:
            for row in text:
                file.write(f"{row}\n")
            print(f"Successfully wrote to {file_name}")
        utils.print_file_contents(file_name)
    except OSError as exception:
        print(f"OSError: {exception}")
        raise


if __name__ == "__main__":
    print(__doc__)
    main()
