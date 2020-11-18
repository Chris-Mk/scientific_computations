# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:07:03 2020

@author: Chris
"""
import matplotlib.pyplot as plt

a = [1/k for k in range(1, 11)]
b = [1/k for k in range(1, 101)]
c = [1/k for k in range(1, 1001)]
d = [1/k for k in range(1, 10001)]
e = [1/k for k in range(1, 100001)]
#y = [n for n in range(1, 18)]


#plt.plot(x, "b.")
#plt.show()

print('a=', sum(a))
print('b=', sum(b))
print('c=', sum(c))
print('d=', sum(d), '\n')

print('e/d=', sum(e)/sum(d))
print('d/c=', sum(d)/sum(c))
print('c/b=', sum(c)/sum(b))
print('b/a=', sum(b)/sum(a))



