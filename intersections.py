# -*- coding: utf-8 -*-
#Given the list of N rocks with their compositions, display the number of gem-elements that exist in those rocks.

N = int(input())
stones = []
for i in range(N):
    stones.append(set(input()))
inter = stones[0].intersection(stones[1])
for i in stones:
    i = set(i)
    inter = i.intersection(inter)
print(len(inter))


# test
# 3
# abcdde
# baccd
# eeabg