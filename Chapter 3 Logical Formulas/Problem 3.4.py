# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:42:14 2018

@author: Administrator
"""

def f(n):
    if n == 1:
        return [["T"], ["F"]]
    else:
        temp = f(n - 1)
        r1 = [i + ["T"] for i in temp]
        r2 = [i + ["F"] for i in temp]
        return r1 + r2
result = f(5)
for i in result:
    print(" ".join(i))