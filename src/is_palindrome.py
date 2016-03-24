# -*- coding: utf-8 -*-
from functools import reduce
import math

def is_palindrome(n):
    '''12321£¬909'''
    return str(n) == str(n)[-1:0]


output = filter(is_palindrome, range(1, 1000))
print(list(output))