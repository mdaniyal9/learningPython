#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 22:21:37 2018

@author: daniyal
"""

import gc
from matrix import Matrix 
#execfile('matrixxx.py')

#matrixxx.a
#matrixxx.b
#matrixxx.Matrix
#matrixxx.np
import numpy as np

a = np.matrix([[1,2,3],[4,5,6]])
b = np.matrix([[9,8,7,6],[5,4,3,2],[1,7,8,9]])   

aa = Matrix(a)

bb = Matrix(b)
#print(bb)
c = aa.multiply(bb)
print(c)
print(aa)

#print(b)
#print(a*b)
#print("My dimensions are"+str(b.shape)+"And data is "+str(b))
gc.collect()
