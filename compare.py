# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:36:39 2020

@author: Chris
"""

a = [1/2**(1/k) for k in range(1, 11)]
b = [1/2**k for k in range(1,11)]

print(sum(a))
print(sum(b))