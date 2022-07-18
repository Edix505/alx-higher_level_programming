#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        r = fct(*args)
    except Exception as x:
        sys.stderr.write("Exception: {}\n".format(x))
        r = None
    return (r)
