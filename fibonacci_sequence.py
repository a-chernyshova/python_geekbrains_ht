# -*- coding: utf-8 -*-
# Python version 3.6.0
# Task:
# Please write a function in any programming language of your choosing (C++, JAVA, Python, VB preferred)
# that will take an integer (n) as a parameter and will find that nth number in the Fibonacci sequence.
# Example Output: 1,1,2,3….n

def fibonacci(n):
    if type(n) == int:
        if n >= 2:
            fibonacci_sequence = [1, 1]
            while len(fibonacci_sequence) < n:
                fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
            for i in fibonacci_sequence:
                print(i, end='')
                if i != fibonacci_sequence[-1]:
                    print(end=', ')
        elif n == 1 or n == 0:
            print(n)
        else:
            print("There is no fibonacci sequence for negative number", n)
    else:
        print("There is no fibonacci sequence for fraction number", n)
