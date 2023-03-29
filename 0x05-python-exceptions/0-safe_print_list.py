#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while my_list[count]:
            if count == x:
                break
            print(my_list[count], end=' ')
            count += 1
    except IndexError:
        print()
    return counit
