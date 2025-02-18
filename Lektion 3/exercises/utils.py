"""Utility functions """

import inspect
import sys

def debug_msg(*args, end="\n"):
    """Utility function. Prints debugging info on stderr"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stderr.write(f"({caller}) {msg}{end}")


def err_msg(*args, end="\n"):
    """Utility function. Prints a(n error) message on stderr"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stderr.write(f"({caller}) {msg}{end}")


def sys_msg(*args, end="\n"):
    """Utility function. Prints a message on stdout"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stdout.write(f"({caller}) {msg}{end}")


