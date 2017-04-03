# -*- coding: utf-8 -*-
# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)
import string


def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)[0:(size)]
    for i in range(size):
        letters = ''
        for l in range(i+1):
            if i == 0:
                letters += (alphabet[size-l-1])
                revers = ''
            elif l == i:
                letters += (alphabet[size-l-1])
                revers = letters[::-1]
                revers = '-'+revers[2:]
            else:
                letters += (alphabet[size-l-1]+'-')
                revers = letters[::-1]
                revers = '-'+revers[2:]
        row = '-'*(2*(size-i)-2) + letters + revers + '-'*(2*(size-i)-2)
        print(row)
    for i in list(range(size-1))[::-1]:
        letters = ''
        for l in range(i+1):
            if i == 0:
                letters += (alphabet[size-l-1])
                revers = ''
            elif l == i:
                letters += (alphabet[size-l-1])
                revers = letters[::-1]
                revers = '-'+revers[2:]
            else:
                letters += (alphabet[size-l-1]+'-')
                revers = letters[::-1]
                revers = '-'+revers[2:]
        row = '-'*(2*(size-i)-2)+letters+revers+'-'*(2*(size-i)-2)
        print(row)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
