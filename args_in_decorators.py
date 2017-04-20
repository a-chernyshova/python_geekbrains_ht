# -*- coding: utf-8 -*-
def decorator_print_args(func_to_decorate):
    def wrapper_for_args(arg1, arg2):
        print('Received arguments: ', arg1+',', arg2)
        func_to_decorate(arg1, arg2)
    return  wrapper_for_args

@decorator_print_args
def print_full_name(arg1, arg2):
    print('My name is', arg1, arg2)


print_full_name("Anastasia", "Nassy")
