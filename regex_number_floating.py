# -*- coding: utf-8 -*-
# The first line contains an integer N, the number of test cases.
# The next N line(s) contains a string T.
# In this task, a valid float number must satisfy all of the following requirements:
# Number can start with +, - or . symbol.
# Number must contain at least  decimal value.
#  Number must have exactly one . symbol.

import re

for i in range(int(input())):
    if re.match(r'^[\+-]?\d*\.\d+$', input()):
        print('True')
    else:
        print('False')
