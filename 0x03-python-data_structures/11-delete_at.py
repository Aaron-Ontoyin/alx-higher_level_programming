#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []
    for cnt, i in enumerate(my_list):
        if cnt != idx:
            new_list.append(i)

    my_list.clear()
    for i in new_list:
        my_list.append(i)
    return my_list
