"""Exercises Lesson 6"""

import json

__all__ = ['DEFAULTS']

try:
    with open("./defaults.json", "r", encoding="utf8") as defaults_file:
        json_data = defaults_file.read()
    DEFAULTS = json.loads(json_data)
except OSError as exception:
    print(f"OSError: {exception}")
except json.JSONDecodeError as exception:
    print(f"JSONDecodeError: {exception}")
