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
        if self.data.shape[1] == other.data.shape[0]:
            return self.data*other.data
        else:
            return "dimension do not match"
    
    def __mul__(self,other):
        if self.data.shape[1] == other.data.shape[0]:
            return self.data*other.data
        else:
            return "dimension do not match"
    
    def __add__(self,other):
        if self.data.shape[0] == other.data.shape[0] and self.data.shape[1] == other.data.shape[1]:
            return self.data+other.data
        else:
            return "dimension do not match"
        
    def __sub__(self,other):
        if self.data.shape[0] == other.data.shape[0] and self.data.shape[1] == other.data.shape[1]:
            return self.data-other.data
        else:
            return "dimension do not match"
    
    def Print(self):
        print("My dimensions are " +str(self.data.shape))
        print("And data is ")
        print(self.data)
        
