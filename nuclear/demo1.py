from matplotlib.pyplot import *
from numpy import *
from scipy.constants import c, m_p, m_n, e


def B(a, z):
    return 15.5e6 * a - 16.8e6 * a ** (2 / 3) - 0.72e6 * z ** 2 * a ** (-1 / 3) - 23e6 * (
                a - 2 * z) ** 2 / a + 12e6 / a ** 0.5


A = 90
Z = linspace(30, 50, 60)
M = (Z * m_p * c ** 2) / e + ((A - Z) * m_n * c ** 2) / e - B(A, Z)
Z_min = A / (1.98 + 0.015 * A ** (2 / 3))

grid()
xlabel("Atomic number Z")
ylabel("Mass M(A, Z)")
plot(Z, M, label="A=90")
legend()
print("Z_min =", Z_min)

# Neutron drip line
# grid()
# xlabel("N")
# ylabel("$S_{n}$ [eV]")
# asd = B(flip(linspace(40, 93, 100)), 40)
# plot(linspace(0, 50, 100), asd)

# Proton drip line
# xlabel("P")
# ylabel("$S_{p}$ [eV]")
# qwe = B(flip(linspace(40, 93, 100)), flip(linspace(0, 41, 100)))
# plot(linspace(0, 41, 100), qwe)
savefig("./graphs/mass_vs_Z.pdf")
