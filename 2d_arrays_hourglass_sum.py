# -*- coding: utf-8 -*-
#Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
#Given a 6*6 2D Array, A:
# Example hourglasses
# a b c
#   d
# e f g
arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
max_sum = sum(arr[0][0:3]) + arr[1][1] + sum(arr[2][0:3])
for i in range(4):
    for y in range(4):
        hourglass = sum(arr[i][y:(y + 3)]) + arr[i + 1][y + 1] + sum(arr[i + 2][y:(y + 3)])
        if hourglass > max_sum :
            max_sum = hourglass

print(max_sum)