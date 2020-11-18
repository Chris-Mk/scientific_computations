import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp

# graph plotting
N = 101
x = np.linspace(-5, 5, N)
y = [1 / (1 + t ** 2) for t in x]

plt.plot(x, y)
plt.show()

# finding approximation
no_of_rectangles = int(input("Number of rectangles: "))


def f(rectangles, base):
    total_sum = 0
    current_base = base

    for i in range(rectangles):
        total_sum += (1 / (1 + current_base ** 2)) * base
        current_base += base
    return total_sum


print(f(no_of_rectangles, 1 / (no_of_rectangles / 2)))
print(sp.quad(lambda x: np.arctan(x), 0, 2))
