from matplotlib.pyplot import *
from numpy import *

N = 50


def energy(momentum):
    return -2 * cos(momentum)


def fermi(E):
    return 1 / (1 + 10 * exp(E))


q = linspace(-5, 5, 100)
w = linspace(-5, 5, 100)
op = zeros((len(q), len(w)))

for i in range(len(w)):
    for j in range(len(q)):
        for kx in range(len(q)):
            for ky in range(len(q)):
                for kz in range(len(q)):
                    pass
                    # term = sum([(fermi(energy(k - q[j])) - fermi(energy(k))) / (energy(k - q[j]) - energy(k) + 1 * w[i] + 0.1j)
                    # for k in range(len(q))])
        # op[i, j] = (1 / N) * term

xlabel('q')
ylabel('$\omega$')
imshow(op, extent=[-5, 5, -5, 5], origin='lower', aspect='auto')
cbar = colorbar()
cbar.set_label('$\Pi(q,\omega)$')

# kinetic_energy = zeros(len(q))
# for i in range(len(q)):
#     numerator = sum([energy(k) * fermi(energy(k)) for k in range(len(q))])
#     denominator = sum([fermi(energy(k)) for k in range(len(q))])
#     kinetic_energy[i] = -numerator / denominator
#
# plot(q, kinetic_energy)

# chi = zeros(len(q))
# for i in range(len(q)):
#     chi[i] = 25 / q[i] ** 2
#
# soln = 1 / (1 - chi * op)
# imshow(soln, extent=[-5, 5, -5, 5])
