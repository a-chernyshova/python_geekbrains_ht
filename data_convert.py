# -*- coding: utf-8 -*-
#Given a time in -hour AM/PM format, convert it to military (-hour) time.


def time_convert(time):
    time = time.strip()
    if int(time[:2]) <= 12 and str(time[-2:]) in ['PM', 'pm', 'am', 'AM']:
        if time[-2:] == 'PM' or time[-2:] == 'pm':
            if time[:2] == '12':
                result = time[:-2]
            else:
                result = str(int(time[:2]) + 12) + time[2:-2]
        elif time[:2] == '12':
            result = '00' + time[2:-2]
        else:
            result = time[0:-2]
        return result
    else:
        return 'Incorrect input: '+time

if __name__ == '__main__':
    print(time_convert('12:05:59PM'))
    print(time_convert('03:05:59PM'))
    print(time_convert('12:05:59AM'))
    print(time_convert('10:05:59pm'))
    print(time_convert('15:05:59pm'))
    print(time_convert('12:05:59'))
