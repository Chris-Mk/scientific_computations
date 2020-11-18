# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:14:51 2020

@author: Chris
"""
import numpy as np

#
# a = [1 / 2 ** k for k in range(100)]
#
# print(sum(a))

matrix = np.arange(15)
print(matrix.shape)

x = np.array([[1, 2, 3, 4], [9, 8, 2, 6]])
y = np.array([(1, 2, 3, 4), (9, 8, 2, 6)])

# a = [[1, 2, 3, 4], [9, 8, 2, 6]]
# b = [(1, 2, 3, 4), (9, 8, 2, 6)]
#
# print(a)
# print(len(b))
# print(a == b)

# print(y.data)
# print(f"x is {x.size} and y is {y.size}")


onesArray = np.ones((2, 2))
zeroArray = np.zeros((2, 2))
randomArray = np.empty((2, 2))

# print(onesArray, zeroArray, randomArray, sep=",\n", end="!!", )
# print(zeroArray)
# print(randomArray)


# duck = np.linspace(1, 5, 25)
# print(duck)

print(type(list(range(1, 10, 3))))
print(type(range(1, 10, 3)))
print(type(np.arange(1, 10, 3)))
print(type(np.array([1, 10, 3])))
print(type(np.linspace(1, 10, 3)))
