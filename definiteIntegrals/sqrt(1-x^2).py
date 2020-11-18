import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp

a = int(input("Lower bound: "))
b = int(input("Upper bound: "))
N = int(input("Number of rectangles: "))


def f(x):
    return (1 - x ** 2) ** (1 / 2)


X = np.linspace(a, b, N + 1)
lower_sum = sum([f(X[k]) * (X[k] - X[k - 1]) for k in range(1, N + 1)])
upper_sum = sum([f(X[k - 1]) * (X[k] - X[k - 1]) for k in range(1, N + 1)])

print(lower_sum)
print(upper_sum)
print(sp.quad(lambda x: (1 - x ** 2) ** (1 / 2), 0, 1))

y = [np.sqrt(1 - i ** 2) for i in X]

plt.plot(X, y)
plt.show()
