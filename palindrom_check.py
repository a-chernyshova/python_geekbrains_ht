# -*- coding: utf-8 -*-
#check if it is a palindrom

def check_palindrom(name):
    name = name.replace(' ', '')
    for i in range(1,len(name)//2+1):
        if name[i-1] != name[-i]:
            return False
    return True

if __name__ == '__main__':
    name1 = 'шалаш'
    name2 = 'base'
    name3 = 'а роза упала на лапу азора'
    print("Is '" + name1 + "' palindrom? -", check_palindrom(name1))
    print("Is '" + name2 + "' palindrom? -", check_palindrom(name2))
    print("Is '" + name3 + "' palindrom? -", check_palindrom(name3))