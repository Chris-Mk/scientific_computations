from sympy import *

theta, phi = symbols('theta phi')
Y00 = 1 / sqrt(4 * pi)
Y11 = -sqrt(3 / (8 * pi)) * sin(theta) * E ** (I * phi)
Y22 = sqrt(15 / (32 * pi)) * (sin(theta)) ** 2 * E ** (I * 2 * phi)

# integrate(conjugate(Y00) * Y11 * sin(theta), (theta, 0, pi), (phi, 0, 2 * pi))
# integrate(conjugate(Y00) * Y00 * sin(theta), (theta, 0, pi), (phi, 0, 2 * pi))
integrate(conjugate(Y11) * Y22 * sin(theta), (theta, 0, pi), (phi, 0, 2 * pi))
