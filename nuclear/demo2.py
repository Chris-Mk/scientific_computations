from matplotlib.pyplot import *
import numpy as np
from scipy.constants import e, pi, epsilon_0
from scipy.stats import linregress

A = np.array([11, 13, 17, 21, 25, 29, 35, 41])
E = (3 / 5) * (e / (4 * pi * epsilon_0 * 1.2e-15)) * A ** (2 / 3)
m, y, r, p, se = linregress(A ** (2 / 3), E)

print(E)
print("Slope =", m)
print("Std error =", se)

grid()
xlabel("$A^{2 / 3}$")
ylabel("$\Delta E$ [eV]")
plot(A ** (2 / 3), E, "ro", label="Data points")
plot(A ** (2 / 3), m * A ** (2 / 3), label="Linear regression")
legend()
savefig("./graphs/EvsA.pdf")
print("r0 =", (3 / 5) * (e / (4 * pi * epsilon_0 * m)))
