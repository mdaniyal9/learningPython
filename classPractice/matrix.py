#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 21:56:49 2018

@author: daniyal
"""



class Matrix(object):
    def __init__(self, data):
        self.data = data
    def multiply(self,other):
        return self.data*other.data
    
    def __str__(self):
        return "My dimensions are"+str((self.data).shape)+"And data is "+str(self.data)