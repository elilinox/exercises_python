# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:48:46 2023

@author: s_schuck20
"""
a = 1
r = 0.5
s = 0
k = 0
limit = a / (1-r)

while True:
    s += a * r**k
    k += 1
    print(s, end = " ")
    if limit-s < 0.01:
        break
