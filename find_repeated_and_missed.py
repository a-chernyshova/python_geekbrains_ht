# -*- coding: utf-8 -*-
import random

#create sequence of integer numbers with 1 missed number and 1 repeated (froom 1 to n)
def create_list(n):
    result_list = list(range(1, n))
    #print(result_list)
    missed_number = random.choice(result_list)
    result_list.remove(missed_number)
    repeated_number = random.choice(result_list)
    result_list.insert(result_list.index(repeated_number), repeated_number)
    return result_list

def find_missed(num_list, n):
    missed = [x for x in list(range(1,n)) if x not in num_list]
    return missed[0]

def find_repeated(num_list):
    repeated = [x for x in num_list if num_list.count(x)>1]
    return repeated[0]


if __name__ == '__main__':
    num_list = create_list(15)
    print(num_list)
    # can be modifyed if we don't know the last number from 1 to len(list)
    print("Missed:",find_missed(num_list, 15))
    print("Repeated:", find_repeated(num_list))