# -*- coding: utf-8 -*-
import sys
#Alice is hosting a party! The party lasts for t minutes, and she puts out a bowl of n
# candies at the beginning of the party. During each minute i, a person comes to the bowl and removes x candies.
# Alice programs the following algorithm into her robot, Bob, to replenish the candy throughout the party:
# If the party is ending (i.e., it's time t), do not refill the bowl.
# If the bowl contains b candies at the end of minute i and b<5, add n-b candies to the bowl.

n,t = map(int, input().strip().split(' '))
c = list(map(int, input().strip().split(' ')))
added = 0
bowl = n
for i in range(t):
    bowl -= c[i]
    if bowl <5 and i != t-1:
        added += n-bowl
        bowl = n

print(added)

#test data:
# 8 4
# 3 1 7 5
# expected result 11