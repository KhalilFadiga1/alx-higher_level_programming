#!/usr/bin/python3
import sys
def safe_function(func, *args):
    try:
        value = func(*args)
        return value
    except Exception as err:
        print("Exception: {}".format(err), file = sys.stderr)
        return None
