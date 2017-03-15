# -*- coding: utf-8 -*-
# Given a base-10 integer, , convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

n = int(input().strip())
n = bin(n)[2:].split('0')
print(len(max(n)))


