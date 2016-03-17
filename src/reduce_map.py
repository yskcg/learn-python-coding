# -*- coding: utf-8 -*-
from functools import reduce
import math

def normalize(name):
   if isinstance(name,str) :
    return name[0].upper()+name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x,y: x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#the first method
def str2float1(s):
    if isinstance(s,str):
        return float(s)

#the second method

char_to_num = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2float(s):
    if isinstance(s,str):
        L = s.split(sep='.')
        def fn(x, y):
            return x*10 + y
        def chartonum(s):
            return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

        if len(L) == 1:
            l1 = reduce(fn, map(chartonum, L[0]))
            return l1
        else:
            if L[0] != '':
                l1 = reduce(fn, map(chartonum, L[0]))
                l2 = reduce(fn, map(chartonum, L[1]))/ (pow(10,len(L[1])))*1.0
                return l1 + l2
            else:
                l2 = reduce(fn, map(chartonum, L[1]))/ (pow(10,len(L[1])))*1.0
                return l2

print('str2float(\'123.456\') =', str2float('123.456'))
print(str2float('0'))
print(str2float('123'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('120.0034'))
