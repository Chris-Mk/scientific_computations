# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:15:45 2020

@author: Chris
"""

import matplotlib.pyplot as plt
import math as m

a = [1/k**2 for k in range(1, 1000)]


plt.plot(a,"b.")
plt.show()

b= m.pi**2/6

#print(a)
print("sum of basel series = ", sum(a))
print("pi squared divided by six = ", b)

print(b-sum(a))