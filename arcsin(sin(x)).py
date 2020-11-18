# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 00:11:14 2020

@author: Chris
"""

import numpy as n
import matplotlib.pyplot as plt
import math as m

a=[m.asin(m.sin(x)) for x in range(-10, 10)]
b=[k for k in range(-10,10)]

plt.plot(b,a)
plt.ylim(-2,2)
plt.xlim(-10, 10)
plt.xticks(5.0)