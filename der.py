import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.tan(x) + 2 * np.log(np.cos(x))


X = np.linspace(2.5, 6.5, 100)
Y = f(X)

plt.plot(X, Y)
plt.show()
