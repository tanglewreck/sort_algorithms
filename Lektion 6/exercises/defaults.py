"""Exercises Lesson 6"""

import json

__all__ = ['load_json']

def load_json():
    """Load defaults from json file"""
    # print(f"cwd: {os.curdir}")
    try:
        with open("defaults.json", "r", encoding="utf8") as file_descriptor:
            data = file_descriptor.read()
            return json.loads(data)
    except json.JSONDecodeError as exception:
        print(f"Error decoding json data: {exception}")
        raise SystemExit(1) from exception
    except OSError as exception:
        print(f"Error reading file: {exception}")
        raise SystemExit(1) from exception
    except TypeError as exception:
        print(exception)
        raise SystemExit(1) from exception
    return None

def main() -> None:
    """main(): read defaults from json file"""
    print(f"{load_json()}")

DEFAULTS = load_json()

# If run from the commandline
if __name__ == "__main__":
    main()
