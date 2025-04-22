"""Utility functions for ball sim"""
import json

__all__ = ["get_defaults"]

def get_defaults():
    """Get defaults"""
    try:
        with open("defaults.json", "r", encoding="utf8") as file_json:
            data_raw = file_json.read()
            data_json = json.loads(data_raw)
            print(data_json)
    except OSError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception
    except json.JSONDecodeError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception
