# -*- coding: UTF-8 -*-


def double_list(input_list):
    "Double all element of list"


    list_lenth=len(input_list)
    for idx in range(list_lenth):
        input_list[idx]*=2

    return

mylist=[1,3,5,7,9]
double_list(mylist)
print(mylist)
