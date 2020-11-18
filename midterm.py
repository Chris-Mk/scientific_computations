import numpy as np
import matplotlib.pyplot as plt

x = -3
N = 20
S = 0

for n in range(0, N + 1):
    S = S + x**n / np.factorial(n)
plt.plot(n, S)
