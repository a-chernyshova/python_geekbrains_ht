# -*- coding: utf-8 -*-
# You are given a string S, containing , and/or . and 0-9 digits.
# Your task is to re.split() all of the , and . symbols.

import re

for i in re.split('[,.]+', input()):
    if i.isdigit():
        print(i)
