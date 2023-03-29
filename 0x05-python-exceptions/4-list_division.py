#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result = []
        for i in range(list_length):
            try:
                elem1 = my_list_1[i]
            except IndexError:
                print("out of range")
                elem1 = 0
            try:
                elem2 = my_list_2[i]
            except IndexError:
                print("out of range")
                elem2 = 0
            try:
                res = elem1 / elem2
                result.append(res)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
    except IndexError:
        print("out of range")
        result.append(0)
    finally:
        return result
