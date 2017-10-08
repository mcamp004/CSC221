# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:42:22 2017

@author: mcamp004
"""


def dx(f, x):
    return abs(0-f(x))
 
def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print ('Root is at: '), x0
    print ('f(x) at root is: '), f(x0)