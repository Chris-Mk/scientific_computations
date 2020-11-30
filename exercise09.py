from numpy import *
from matplotlib.pyplot import *


class Polygon:

    def __init__(self, A, B, C, D):
        self._A = array(A)
        self._B = array(B)
        self._C = array(C)
        self._D = array(D)
        self._h = self._A - self._B
        self._w = self._A - self._C

    def get_height(self):
        return self._h

    def get_width(self):
        return self._w

    def plot(self):
        plot([self._A[0], self._B[0], self._C[0], self._D[0], self._A[0]],
             [self._A[1], self._B[1], self._C[1], self._D[1], self._A[1]])
        grid()
        show()


class Rectangle(Polygon):

    def area(self):
        return cross(self.get_height(), self.get_width())

    def __contains__(self, other):
        return other.area() < self.area()


r1 = Rectangle([1, 2], [4, 2], [4, 5], [1, 5])
r2 = Rectangle([2, 3], [3, 3], [3, 4], [2, 4])

print(r2 in r1)
print(r1.area())
print(r2.area())
# subplot(2, 1, 1)
r1.plot()
# subplot(2, 1, 2)
r2.plot()

#
# class SpecialRectangle(Rectangle):
#
#     def edges_parallel_to_axes(self):
#         pass
