# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:11:56 2023

@author: s_schuck20
"""
x = "Hallo, Berlin"
list(x)
print(list(x))


def buchstaben_zählen(x):
    count_letters = []
    meine_liste = list(x)
    for buchstabe in meine_liste:
        if buchstabe.isalpha()==True:
            count_letters.append(1)
        else:
           count_letters.append(0)
    return sum(count_letters)
    
print(buchstaben_zählen(x))