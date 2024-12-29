import matplotlib.pyplot as plt
import numpy as np

# Données
# L = np.array([100, 110, 120, 130, 140])
L = np.array([98, 116, 158])
amp = np.array([0.004674, 0.006228, 0.007698])

# amp = np.array([0.005849, 0.005793, 0.008676, 0.006684, 0.003638])
# amp = np.array([1 - 0.983190, 1 - 0.990359, 1 - 0.975665, 1 - 0.983370, 1 - 0.966634])

# Ajustement polynomial de degré 1 (ajustement linéaire)
p = np.polyfit(L, amp, 1)

# Affichage des coefficients du polynôme ajusté
print(f'Coefficients du polynôme ajusté (pente, intercept) : {p}')

# Calcul de L0 à partir des coefficients du polynôme
L0 = (1 - p[1]) / p[0]
# L0 = (1 - 2.89e-4) / 3.24e-3
print(f'L0 = {L0:.6f}')

# Tracé des données
plt.figure()
plt.plot(L, amp, 'r*', label='data')
plt.xlabel('L [cm]')
plt.plot(L, p[0] * L + p[1], label='linear fit')
x = np.linspace(-20, 100, 200)
plt.plot(x, p[0] * x + p[1], 'r--', label='Extrapolation')
plt.legend()
plt.ylabel('Amplitude')
plt.title('Amplitude vs L')
plt.grid(True)
plt.show(block=True)
