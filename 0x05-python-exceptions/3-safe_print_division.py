#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    except TypeError:
        print("Error: invalid types")
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
