#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:36:13 2018

@author: lucasnn
"""

import numpy as np


def ler_instancias(file_name):
        
    with open(file_name, "r") as file:
        a_np = np.array([i.split() for i in file.read().split("\n")[:-1]]).transpose().astype("int")

    return a_np

   
file_names  = ["mochila02.txt", "mochila01.txt", "mochila1000.txt", "mochila2500.txt", "mochila5000.txt"]

mochilas = list()

for name in file_names:
    #mochilas = np.append(mochilas,ler_instancias(name))
    mochilas.append(ler_instancias(name))