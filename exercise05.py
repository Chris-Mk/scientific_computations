import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

# =============================================================================
# task 01 & 02
# =============================================================================

omega = np.linspace(0, 2 * np.pi, 1000)
integrals = [quad(lambda x: np.sin(w * x), 0, np.pi / 2) for w in omega]

plt.plot(omega, integrals)
plt.show()

# =============================================================================
# task 03
# =============================================================================

print(fsolve(lambda x: x ** 2 + x - 3, 1))

# =============================================================================
# task 04
# =============================================================================

a = range(1, 5)
zeros = [fsolve(lambda x: i * x ** 2 + x - 3, 1) for i in a]

plt.plot(zeros, a)
plt.show()
