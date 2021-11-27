from numpy import *
from numpy.linalg import inv
from scipy.optimize import fmin

A = array([[1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1]])
b = array([1, -1, 1, -1])

A_trans = A.transpose()
lhs = A_trans.dot(A)
rhs = A_trans.dot(b)

print("X = ", inv(lhs).dot(rhs))
print(fmin(lambda x: linalg.norm(A.dot(x) - b), array([1, 1, 1])))


