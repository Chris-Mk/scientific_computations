import matplotlib.pyplot as plt
import numpy as np

# Données
L = np.array([100, 110, 120, 130, 140])
amp = np.array([0.983189546496463, 0.9903587884793253, 0.9756649537998469, 0.983370086905421, 0.9666336655719123])

# Adjustment polynomial degree 1 (adjustment linear)
p = np.polyfit(L, amp, 1)

# Tracé des données
plt.figure()
plt.plot(L, amp, 'r*', label='data')
plt.xlabel('L [cm]')
plt.plot(L, p[0] * L + p[1], label='linear fit')
# x = np.linspace(0, 100, 200)
# plt.plot(x, p[0] * x + [1], 'r--', label='Extrapolation')
plt.legend()
plt.ylabel('Amplitude')
plt.title('Amplitude vs L')
plt.grid(True)
plt.show(block=True)

# Affichage des coefficients du polynôme ajusté
print(f'Coefficients du polynôme ajusté (pente, intercept) : {p}')

# Calcul de L0 à partir des coefficients du polynôme
L = (1 - p[1]) / p[0]
print(f'L = {L:.6f}')
