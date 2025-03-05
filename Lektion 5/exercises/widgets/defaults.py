"""Load default values for widgets from json file"""

import json

__all__ = ["DEFAULTS"]

def save_json():
    """Save defaults to file in json format"""
    # defaults_json = json.dumps(DEFAULTS)
    try:
        with open("defaults.json", "w", encoding="utf8") as file_descriptor:
            json.dump(DEFAULTS, file_descriptor)
    except OSError as exception:
        print(f"Error: {exception}")


def load_json():
    """Load defaults from json file"""
    with open("defaults.json", "r", encoding="utf8") as file_descriptor:
        data = file_descriptor.read()
        return json.loads(data)
    return None


# Load defaults for widgets from file
try:
    DEFAULTS = load_json()
except json.JSONDecodeError as exception:
    print(f"Error decoding json data: {exception}")
    raise SystemExit(1) from exception
except OSError as exception:
    print(f"Error reading file: {exception}")
    raise SystemExit(1) from exception
except TypeError as exception:
    print(exception)
    raise SystemExit(1) from exception


# If run from the commandline
if __name__ == "__main__":
    pass
