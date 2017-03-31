# -*- coding: utf-8 -*-
# create sequence of integer numbers with 1 missed number and 1 repeated (froom 1 to n)
import random


def create_list(n):
    result_list = list(range(1, n+1))
    missed_number = random.choice(result_list)
    result_list.remove(missed_number)
    repeated_number = random.choice(result_list)
    result_list.insert(result_list.index(repeated_number), repeated_number)
    return result_list


def find_missed_and_repeated(num_list):
    missed = ''
    repeated = ''
    for i in list(range(1, len(num_list))):
        if i not in num_list:
            missed = i
        elif num_list.count(i) > 1:
            repeated = i
    return 'Missed: '+str(missed) + ',' + 'Repeated: '+str(repeated)


if __name__ == '__main__':
    num_list = create_list(15)
    print(num_list)
    # can be modified if we don't know the last number from 1 to len(list)
    print(find_missed_and_repeated(num_list))
