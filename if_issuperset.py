# -*- coding: utf-8 -*-
# You are given one set  and a number of other sets, .
# Your job is to find whether set  is a strict superset of all the  sets.
# Print True, if  is a strict superset of all of the  sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.

A = set(map(int, input().split()))
N = int(input())

def issuper(A, N):
    for i in range(N):
        if A.issuperset(list(map(int, input().split()))):
            pass
        else:
            return False
    return True

print(issuper(A, N))