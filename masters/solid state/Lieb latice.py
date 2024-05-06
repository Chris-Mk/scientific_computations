from matplotlib.pyplot import *
from numpy import *
from numpy.linalg import eig

N, t, a = 3, -0.5, 2
zeros = np.zeros((1, N))[0]
H = t * np.diag(zeros)


def hamiltonian(x, y):
    # H[0, 0] = 0.5  # for open boundary condition
    H[0, 1] = 1 + exp(-2j * a * x)
    H[1, 0] = 1 + exp(2j * a * x)
    H[0, -1] = 1 + exp(-2j * a * y)
    H[-1, 0] = 1 + exp(2j * a * y)
    return H


kx, ky = linspace(0, pi / (2 * a), 100), linspace(0, pi / (2 * a), 100)
energies = []
for i in range(0, len(kx)):
    g = eig(hamiltonian(kx[i], 0))[0]
    x = eig(hamiltonian(pi / (2 * a), ky[i]))[0]
    m = eig(hamiltonian(flip(kx)[i], flip(ky)[i]))[0]
    energies.append([g, x, m])

energies = array(energies)

# plots for energy-momentum dispersion relation
plot(linspace(0, 1, 300), concatenate([energies[:, 0][:, 0], energies[:, 1][:, 0], energies[:, 2][:, 0]]), 'g')
plot(linspace(0, 1, 300), concatenate([energies[:, 0][:, 1], energies[:, 1][:, 1], energies[:, 2][:, 1]]))
plot(linspace(0, 1, 300), concatenate([energies[:, 0][:, 2], energies[:, 1][:, 2], energies[:, 2][:, 2]]))
xlabel('k')
ylabel('E')

# plots for density of states (DOS)
# E = concatenate([
#     concatenate([energies[:, 0][:, 0], energies[:, 1][:, 0], energies[:, 2][:, 0]]),
#     concatenate([energies[:, 0][:, 1], energies[:, 1][:, 1], energies[:, 2][:, 1]]),
#     concatenate([energies[:, 0][:, 2], energies[:, 1][:, 2], energies[:, 2][:, 2]])
# ])
#
# hist_values, bin_edges = np.histogram(E, bins=50)
# hist(E, bins=bin_edges, align='mid', density=True)
# xlabel('E')
# ylabel('DOS')
# text(0.2, 3.2, 'Van Hove Singularity')
# text(1.2, 0.5, 'Van Hove Singularity')
# text(-2.9, 0.5, 'Van Hove Singularity')
