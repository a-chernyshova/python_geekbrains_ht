# -*- coding: utf-8 -*-
# Task-1: Given list of int numbers, need to get new list. Elements of this list are Square root of parent list.
# Requirements: if it is possible to get square root and if square root is int
# Example: given: [2, -5, 8, 9, -25, 25, 4]   Result: [3, 5, 2]
import random
import math
import time
from datetime import datetime, date

def second_root(list):
    for i in list:
        if i<0:
            list.remove(i)
    x = 0
    for i in list:
        if float.is_integer(math.sqrt(i)):
            list[x] = int(math.sqrt(i))
            x += 1
        else:
            list.remove(i)
    list.remove(list[x])
    return list

print("Task#1")
list1=[2, -5, 8, 9, -25, 25, 4]
print(second_root(list1))

# Task-2: Given date dd.mm.yyyy, for example: 02.11.2013.
# Need to show it in text form (второе ноября 2013 года)
days = {
        1:'первое', 2:'второе', 3:'третье', 4:'четвертое', 5:'пятое', 6:'шестое', 7:'седьмое', 8:'восьмое', 9:'девятое',
        10:'десятое', 11:'одиннадцатое', 12:'двенадцатое', 13:'тринадцатое', 14:'четырнадцатое', 15:'пятнадцатое', 16:'шестнадцатое',
        17:'семнадцатое', 18:'восемнадцатое', 19:'девятнадцатое', 20:'двадцатое', 21:'двадцать первое', 22:'двадцать второе',
        23:'двадцать третье', 24:'двадцать четвертое', 25:'двадцать пятое', 26:'двадцать шестое', 27:'двадцать седьмое',
        28:'двадцать восьмое', 29:'двадцать девятое', 30:'тридцатое', 31:'тридцать первое'}
months = {
        1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь',
        11:'ноябрь', 12:'декабрь'}
#list_date=input('input date here dd.mm.yyyy:')
#list_date = list_date.split('.')
#day_text = list_date[0]
#month_text = list_date[1]
#for i in list_date:
#    if i in day.keys():
#         print(day[i])

# Task-3: Fill set by random int numbers (-100 до 100). There must be n elements in list.
def random_list(n):
    list=[]
    for i in range(n):
        list.append(random.randint(-100, 100))
    return list
print('Task#3')
print(random_list(int(input("введи число"))))

# Task-4: Given list of int numbers. Need to get new list consists from unique elemets from the first one.
list1 = [1, 5, 10, 15, 5, 1, 5, 2]
list2 = set(list1)
print("Task#4")
print(list2)

#HARD
# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

#equation = 'y = -12x + 11111140.2121'
#x = 2.5
# вычислите и выведите y

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'