# -*- coding: utf-8 -*-
import math
# Task-1: Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    _list = [1, 1]
    x = 1
    for i in range(m-2):
        _list.append(_list[x] + _list[x-1])
        x +=1
    return _list[n:]
print('task#1')
print(fibonacci(1, 5))
print(fibonacci(3, 10))
print(fibonacci(5, 15))

# Task-2:
# Wtite function sorting list in ascending order.
# You shouldn't use sort()

def sort_to_max(origin_list):
    for n in range(len(origin_list)-1):
        x = 1
        for i in origin_list[:-1]:
            if i > origin_list[x]:
                origin_list[x], origin_list[x-1] = origin_list[x-1], origin_list[x]
            x +=1
    return(origin_list)
print('task#2')
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

#the second solution
def sort_to_max1(origin_list):
    _list = []
    for i in range(len(origin_list)):
        _list.append(min(origin_list))
        origin_list.remove(min(origin_list))
    return(_list)
print('task#2')
print(sort_to_max1([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Task-3:
# Write your own solution for function filter
# You shouldn't use function filter
def _filter(func, _list):
    result = []
    for i in _list:
        if func(i):
            result.append(i)

    return result

print('#task3')
a = [1,2,5,6,8,9,10]

print(_filter(lambda x: x%2==0, a))

# Task-4:
# Given 4 points А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Need to calculate: could they be 	peaks of parallelogram

def _isparalm(x, y, w, z):
    dlina1 = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    dlina2 = math.sqrt((z[0] - w[0])**2 + (z[1] - w[1])**2)
    if dlina1 == dlina2:
        return True
    else:
        return False
print("task#4")
print(_isparalm([1,2], [2,4], [5,4], [4,2]))
print(_isparalm([0,1], [1,1], [2,1], [1,2]))
print(_isparalm([3,4], [2,1], [3,4], [2,1]))
print(_isparalm([1,2], [3,4], [5,2], [0,3]))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов
# Записать в новые файлы все фрукты начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание что нет фруктов начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
