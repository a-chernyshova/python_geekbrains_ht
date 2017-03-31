# -*- coding: utf-8 -*-
# The first line contains an integer, n, denoting the number of elements in array a.
# The second line contains n space-separated integers describing a


def bubble_sorting(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swaps += 1
    print('Array is sorted in', swaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    bubble_sorting([3, 2, 1])
    bubble_sorting(a=[int(a_temp) for a_temp in input().strip().split(' ')])
