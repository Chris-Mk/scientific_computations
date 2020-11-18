# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:00:25 2020

@author: Chris
"""
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    x_cos = np.cos(x)
    return np.tan(x) + np.log(x_cos) * 2


X = np.linspace(0, 1, 100)
Y = f(X)

plt.plot(X, Y)
plt.title('Graph of tan(x)+2ln(cos(x))')
plt.show()
# print(np.tan(np.deg2rad(45)))
