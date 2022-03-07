from sympy import *

Z = 11
r = symbols('r')
ao = 5.29e-11
R1s = 2 * (Z / ao) ** (3 / 2) * E ** (-(Z * r) / ao)

ans = 1 - integrate(R1s ** 2 * r ** 2, (r, 0, ao / 11))
print(ans)

# r = ao / Z
# P1s = 2 * Z ** (3 / 2) * r * E ** (-Z * r)

# P2s = (1 / sqrt(2)) * Z ** (3 / 2) * r * E ** ((-Z * r) / 2) * (1 - 0.5 * Z * r)
# P2p = (1 / (2 * sqrt(6))) * Z ** (5 / 2) * r ** 2 * E ** ((-Z * r) / 2)
# P3s = (2 / (3 * sqrt(3))) * Z ** (3 / 2) * r * E ** ((-Z * r) / 3) * (1 - (2 / 3) * Z * r + (2 / 27) * (Z * r) ** 2)
# P3p = (8 / (27 * sqrt(6))) * Z ** (5 / 2) * r ** 2 * E ** ((-Z * r) / 3) * (1 - (1 / 6) * Z * r)
# P3d = (4 / (81 * sqrt(30))) * Z ** (7 / 2) * r ** 3 * E ** ((-Z * r) / 3)

# integrate(r * P1s ** 2, (r, 0, oo))
# integrate(r * P2s ** 2, (r, 0, oo))
# integrate(r * P2p ** 2, (r, 0, oo))
# integrate(r * P3s ** 2, (r, 0, oo))
# integrate(r * P3p ** 2, (r, 0, oo))
# integrate(r * P3d ** 2, (r, 0, oo))

# integrate(R1s ** 2 * r ** 2, (r, 0, ao / 11))
# integrate(P1s ** 2 * r ** 2, (r, 0, oo))
# ans = 1 - integrate(R1s ** 2 * r ** 2, (r, 0, ao / 11))
# print(ans)
# print(P1s ** 2 * r ** 2)
