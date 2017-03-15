# -*- coding: utf-8 -*-
# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.
# A valid mobile number is a ten digit number starting with 7-9 (10 digits).

import re

N = int(input())
for i in range(N):
    print(('YES') if re.match(r'[7-9]\d{9}$', input()) else 'NO')
