# -*- coding: utf-8 -*-
# The first line of input contains an integer N, the number of mobile phone numbers.
# N lines follow each containing a mobile number.
# +91 xxxxx xxxxx
#The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number.
# Alternatively, there may not be any prefix at all.

def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
        # for i in l:
        #     if len(i) == 10:
        #         print('+91', i[:5], i[5:])
        #     elif len(i) == 11:
        #         print('+91', i[1:6], i[6:])
        #     else:
        #         print('+91', i[2:7], i[7:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    #l = [input() for _ in range(int(input()))]
    l = ['07895462130', '919875641230', '9195969878']
    sort_phone(l)
