from numpy import *
from matplotlib.pyplot import *


class Interval:
    """
    Interval(real number) -> Interval object
    Creates an interval object containing a single input value

    Interval(startpoint, endpoint) -> Interval object
    Creates an interval object containing all values between and including the
    input values

    Raises exception for a number of input values not equal to 1 or 2
    """

    def __init__(self, *args):
        if len(args) == 1:
            self._startpoint = args[0]
            self._endpoint = args[0]
        elif len(args) == 2:
            self._startpoint = args[0]
            self._endpoint = args[1]
        else:
            raise Exception("Wrong number of arguments!")

    """
    Returns the startpoint
    """

    def get_startpoint(self):
        return self._startpoint

    """
    Returns the endpoint
    """

    def get_endpoint(self):
        return self._endpoint

    """
    Returns the sum of an interval and an object of type integer, float or interval
    """

    def __add__(self, other):
        a, b = self.get_startpoint(), self.get_endpoint()
        if isinstance(other, int) or isinstance(other, float):
            return Interval(a + other, b + other)
        else:
            c, d = other.get_startpoint(), other.get_endpoint()
        return Interval(a + c, b + d)

    """
    Returns the sum of an integer or float and an interval
    """

    def __radd__(self, other):
        return self + other

    """
    Returns the difference of an interval and an object of type integer, float or interval
    """

    def __sub__(self, other):
        a, b = self.get_startpoint(), self.get_endpoint()
        if isinstance(other, int) or isinstance(other, float):
            return Interval(a - other, b - other)
        else:
            c, d = other.get_startpoint(), other.get_endpoint()
        return Interval(a - d, b - c)

    """
    Returns the difference of an integer or float and an interval
    """

    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            a, b = self.get_startpoint(), self.get_endpoint()
            return Interval(min([other - a, other - b]), max([other - a, other - b]))
        else:
            return other - self

    """
    Returns the product of an interval and an object of type integer, float or interval
    """

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            a, b = self.get_startpoint(), self.get_endpoint()
            return Interval(a * other, b * other)
        else:
            a, b = self.get_startpoint(), self.get_endpoint()
            c, d = other.get_startpoint(), other.get_endpoint()
        return Interval(min([a * c, a * d, b * c, b * d]), max([a * c, a * d, b * c, b * d]))

    """
    Returns the product of an integer or float and an interval
    """

    def __rmul__(self, other):
        return self * other

    """
    Returns the quotient of an interval and an object of type integer, float or interval
    """

    def __truediv__(self, other):
        a, b = self.get_startpoint(), self.get_endpoint()
        c, d = other.get_startpoint(), other.get_endpoint()

        if 0 in other or abs(a - b) >= inf or abs(c - d) >= inf:
            raise ArithmeticError("Division not possible!")
        return Interval(min([a / c, a / d, b / c, b / d]), max([a / c, a / d, b / c, b / d]))

    """
    Returns a string representation of an interval
    """

    def __repr__(self):
        a, b = self.get_startpoint(), self.get_endpoint()
        return f"[{a}, {b}]"

    """
    Checks if a number is contained in an interval
    """

    def __contains__(self, num):
        a, b = self.get_startpoint(), self.get_endpoint()
        return True if a <= num <= b else False

    """
    Implements the power function for intervals
    """

    def __pow__(self, exponent):
        a, b = self.get_startpoint(), self.get_endpoint()
        if exponent % 2 == 0:
            if a >= 0:
                return Interval(a ** exponent, b ** exponent)
            elif b < 0:
                return Interval(b ** exponent, a ** exponent)
            else:
                return Interval(0, max([a ** exponent, b ** exponent]))
        else:
            return Interval(a ** exponent, b ** exponent)


# %%
"""
Task 4
"""
I1 = Interval(1, 4)
I2 = Interval(-2, -1)
# I2 = Interval(-2, 1) # raises an exception

print(I1)  # [1, 4]
print(I2)  # [-2, -1]
print(I1 + I2)  # [-1, 3]
print(I1 - I2)  # [2, 6]
print(I1 * I2)  # [-8, -1]
print(I1 / I2)  # [-4.,-0.5]

# %%%
"""
Task 8
"""
print(Interval(2, 3) + 1)  # [3, 4]
print(1 + Interval(2, 3))  # [3, 4]
print(1.0 + Interval(2, 3))  # [3.0, 4.0]
print(Interval(2, 3) + 1.0)  # [3.0, 4.0]
print(1 - Interval(2, 3))  # [-2, -1]
print(Interval(2, 3) - 1)  # [1, 2]
print(1.0 - Interval(2, 3))  # [-2.0, -1.0]
print(Interval(2, 3) - 1.0)  # [1.0, 2.0]
print(Interval(2, 3) * 1)  # [2, 3]
print(1 * Interval(2, 3))  # [2, 3]
print(1.0 * Interval(2, 3))  # [2.0, 3.0]
print(Interval(2, 3) * 1.0)  # [2.0, 3.0]

# %%
"""
Task 9
"""
x = Interval(-2, 2)
print(x)  # [-2,2]
print(x ** 2)  # [0,4]
print(x ** 3)  # [-8,8]

# %%
"""
Task 10
"""

xl = linspace(0., 1, 1000)  # An array of startpoints for the interval I

xu = linspace(0.5, 1.5, 1000)  # An array of endpoints for the interval I


def p(x):  # The polynomial given in the exercise
    return 3 * x ** 3 - 2 * x ** 2 - 5 * x - 1


yl = []  # A list of the lower boundaries of a new interval
yu = []  # A list of the upper boundaries of a new interval

"""
Creates a new interval for each interval with the lower boundary in xl and the
upper boundary in xu by running it through the function p(x). Appends the
lower boundary of each interval to yl and the upper one to yu.
"""

for i in range(len(xl)):
    I = Interval(xl[i], xu[i])
    new_I = p(I)
    yl.append(new_I.get_startpoint())
    yu.append(new_I.get_endpoint())

plot(xl, yl, label="yl")  # plots the lower boundaries of the new interval
plot(xl, yu, label="yu")  # plots the upper boundaries of the new interval

xlabel("x")
ylabel("p(I)")
title("$p(I)=3I^3-2I^2-5I-1$, I = Interval(x, x+0.5)")
xlim(0.0, 1.0)
ylim(-10, 4)
legend()
