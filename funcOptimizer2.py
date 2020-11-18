import math as m
import matplotlib.pyplot as plt

x = [a for a in range(-10, 10)]
y = [m.fabs(b ** 2 + b - 2) for b in range(-10, 10)]

plt.plot(x, y)
plt.show()
