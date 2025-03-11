"""Utility functions"""

__all__ = ['print_file_contents']

def print_file_contents(file_name):
    """Open a file and print its contents to stdout"""
    try:
        with open(file_name, 'r', encoding="utf8") as file:
            print("foo")
            print(file.read())
    except OSError as exception:
        print(f"Error reading {file_name}: {repr(exception)}") 
