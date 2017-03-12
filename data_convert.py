# -*- coding: utf-8 -*-
#Given a time in -hour AM/PM format, convert it to military (-hour) time.
# time = input().strip()
# if time[-2:] == 'PM':
#     if time[:2] == '12':
#         result = time[:-2]
#     else:
#         result = str(int(time[:2]) + 12) + time[2:-2]
# elif time[:2] == '12':
#     result = '00' + time[2:-2]
# else:
#     result = time[0:-2]
# print(result)

def foo(data):
    if data < 0:
        return
    yield 10
    return 1
print(foo(-1))