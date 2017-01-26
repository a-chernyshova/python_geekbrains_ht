# -*- coding: utf-8 -*-
# Task-1: List of fruits. Build a program wich show numerated right-aligned list of fruits

def format_list(list):
    max_len = 2
    for i in list:
        if len(i) > max_len:
            max_len=len(i)
    for i,x  in enumerate(list, 1):
        print('{}.{:>{max_len}}'.format(i, x, max_len=max_len))

list = ['apple', 'orange', 'sdfsdfdsfsdfsdfsdfsd', 'berry', '', 'er']
print('Task#1')
format_list(list)

# Task-2:
# You have 2 lists. Need to remove all elements of 2nd list from the first list
def remove_repeated(list1, list2):
    for i in list2[:]:
        while i in list1:
            list1.remove(i)
    print(list1)
    return list1

print('Task#2')
list1 = [2, 14, 10, 'a', 'qa', '', 1, 14]
list2 = [14, 10, 'qa', '']
remove_repeated(list1, list2)

# Task-3:
# You have any list of int numbers. Need to get new list appropriate to requirements:
# if even then divide it 4, else multiply 2

def change_list(list):
    x = 0
    for i in list:
        if i%2 == 0:
            list[x] = i/4
            x += 1
        else:
            list[x] = i*2
            x += 1
    return list

list3 = [4, 5, 8, 10, 0, 1, 50, 4, 1]
print('Task#3')
print(change_list(list3))
