from matplotlib.pyplot import *
from numpy import *

data = loadtxt('./masters/solid state/kramerskronig.txt')
omega, Re_a, Re_b = data[:, 0], data[:, 1], data[:, 2]

# Real part of chi
xlabel('$\omega$')
# ylabel('Re{$\chi(\omega)$}')
# plot(omega, Re_a, label='Re{$\chi_a$}')
# plot(omega, Re_b, label='Re{$\chi_b$}')
# legend()

Im_a = Im_b = zeros(len(omega))
for o in range(len(omega)):
    a_array = b_array = zeros(len(omega))
    for i in range(len(omega)):
        if omega[i] != omega[o]:
            a_array[i] = Re_a[i] / (omega[i] - omega[o])
            b_array[i] = Re_b[i] / (omega[i] - omega[o])
    Im_a[o] = -1 / pi * (omega[1] - omega[0]) * sum(a_array)
    Im_b[o] = -1 / pi * (omega[1] - omega[0]) * sum(b_array)

# Imaginary part of chi
ylabel('Im{$\chi(\omega)$}')
plot(omega, Im_a, label='Im{$\chi_a$}')
plot(omega, Im_b, label='Im{$\chi_b$}')
legend()
