"""= = = = = =
Exercise 4
= = = = = = """

import os
import subprocess
import utils
from defaults import DEFAULTS

__all__ = ['exercise_4_main']

def exercise_4_main():
    """main of exercise 4"""
    def copy_file_1(file: str = None, copy: str = None) -> str:
        """Copy file using read() and write()"""
        with open(file, 'r', encoding="utf8") as fd_one:
            with open(copy, 'w', encoding="utf8") as fd_two:
                file_data = fd_one.read()
                fd_two.write(file_data)

    def copy_file_2(file: str = None, copy: str = None) -> str:
        """Copy a file using subprocess.check_call"""
        if os.path.exists("/bin/cp"):
            cp = ["/bin/cp", file, copy]
        elif os.path.exists("/usr/bin/cp"):
            cp = ["/usr/bin/cp", file, copy]
        else:
            raise OSError("Unable to locate 'cp' command: copy_file_2() failed")
        out = subprocess.check_call(cp)
        return out

    print(__doc__)
    file_name = DEFAULTS['files']['fileName']
    file_copy_1 = DEFAULTS['files']['fileNameCopyOne']
    file_copy_2 = DEFAULTS['files']['fileNameCopyTwo']
    try:
        # Copy 1
        copy_file_1(file_name, file_copy_1)
        print(f"Successfully copied {file_name} to {file_copy_1}")
        utils.print_file_contents(file_copy_1)

        # Copy 2
        print()
        copy_file_2(file_name, file_copy_2)
        print(f"Successfully copied {file_name} to {file_copy_2}")
        utils.print_file_contents(file_copy_2)

    except subprocess.CalledProcessError as exception:
        print(f"{exception}")
    except OSError as exception:
        print(f"{exception}")

if __name__ == "__main__":
    exercise_4_main()
