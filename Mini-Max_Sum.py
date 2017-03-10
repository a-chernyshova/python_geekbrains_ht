# -*- coding: utf-8 -*-
#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
#of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

# lista = [a, b, c, d, e]
# mini, maxi = sum(lista), a
# for i in range(5):
#     summa = sum(lista) - lista[i]
#     if summa > maxi:
#         maxi = summa
#     elif summa < mini:
#         mini = summa

sorted_list = sorted([a, b, c, d, e])
maxi = sum(sorted_list) - sorted_list[0]
mini = sum(sorted_list) - sorted_list[-1]

print(maxi, mini)