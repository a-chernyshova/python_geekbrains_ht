# -*- coding: utf-8 -*-
# Task-1: # Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).Не используйте встроенные и функции и функции из модуля math
def my_round(number, ndigits):
    parts = (str(number)).split('.')
    fraction = parts[1][:(ndigits+1)]
    integer = int(parts[0])
    set_digits = []
    for i in fraction:
        set_digits.append(int(i))
    reversed_set = set_digits[::-1]
    if reversed_set[0] > 5:
        x = 0
        reversed_set[1] += 1
        reversed_set = reversed_set[1:]
        for i in reversed_set:
            x += 1
            if i == 10:
                reversed_set[x-1] = 0
                if x == len(reversed_set):
                    integer +=1
                else:
                    reversed_set[x] += 1
        fraction = reversed_set[::-1]
    else:
        pass
    str_fr = ''
    for i in fraction:
        str_fr += str(i)
    number = str(integer) + '.' + str_fr
    return number

print('Task#1')
print(my_round(2.1299987, 5))
print(my_round(5.99987, 3))

# Task-2: # Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    sum_1 = 0
    sum_2 = 0
    set_digits = []
    for i in str(ticket_number):
        set_digits.append(int(i))
    for i in set_digits[:3]:
        sum_1 += i
    for i in set_digits[3:]:
        sum_2 += i
    return sum_1 == sum_2

print('Task#2')
print(lucky_ticket(125639))
print(lucky_ticket(156561))