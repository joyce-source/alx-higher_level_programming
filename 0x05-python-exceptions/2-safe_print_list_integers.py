#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while True:
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end=' ')
                count += 1
            i += 1
            if count == x:
                break
        except:
            break
    print()
    return count

