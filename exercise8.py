# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:16:09 2023

@author: s_schuck20
"""
example="Berlin"

def vokon_zählen(example):
    count = 0
    zählen = 0
    for i in range(len(example)):
        if (
            (example[i] == "a")
            or (example[i] == "e")
            or (example[i] == "i")
            or (example[i] == "o")
            or (example[i] == "u")
        ):
            count += 1
        else:
            zählen +=1
    print("Es gibt",count, "Vokale und", zählen, "Konsonanten")
vokon_zählen(example)
