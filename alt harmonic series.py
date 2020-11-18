# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:53:06 2020

@author: Chris
"""

a = [((-1)**(k+1))/k for k in range(1, 101)]

print(a)
print(sum(a))