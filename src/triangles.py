# -*- coding: utf-8 -*-

def triangles():
    n = 0
    L = [1]
    while 1 :
        yield L
        L.append(1)
        L[1:-1] = [item +L[i+1] for i,item in enumerate(L[:-2])]
n= 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break