import matplotlib.pyplot as plt
import numpy as np
from math import factorial
import scipy.integrate as integrate
from scipy.special import eval_hermite

#%%
a = 0.000001
def psi(n,x):
    x = x + a/2
    return 1/(2**n * factorial(n))**(1/2) * (1/np.pi)**(1/4) * np.exp(-(x**2)/2) * eval_hermite(n, x)

def phi(n,x):
    x = x - a/2
    return 1/(2**n * factorial(n))**(1/2) * (1/np.pi)**(1/4) * np.exp(-(x**2)/2) * eval_hermite(n, x)



#%%
def transition_dipole_moment(n, m, a):
    def integrand(x):
        return psi(n,x) * x * phi(m, x)
    
    result, error = integrate.quad(integrand, -np.inf, np.inf)
    print(result)
    return result


# Define the quantum numbers range
max_n_m = 9
n_values = np.arange(0, max_n_m + 1)
m_values = np.arange(0, max_n_m + 1)
dipole_moments = np.zeros((max_n_m + 1, max_n_m + 1))

# Compute the dipole moments
for i, n in enumerate(n_values):
    for j, m in enumerate(m_values):
        dipole_moments[i, j] = transition_dipole_moment(n, m, a)

# # Create the contour plot
# plt.figure(figsize=(8, 6))
# contour_plot = plt.contourf(n_values, m_values, dipole_moments)
# plt.colorbar(contour_plot)
# plt.title('Transition Dipole Moments as a Function of n and m')
# plt.xlabel('Quantum Number n')
# plt.ylabel('Quantum Number m')
# plt.grid(True)
# plt.show()

#%%

plt.figure(figsize=(8, 6))
plt.imshow(dipole_moments, extent=[0, max_n_m, 0, max_n_m], origin='lower', cmap='viridis', aspect='auto')
plt.colorbar()
plt.title(r'$\mu_{nm} = \langle \psi_n | \hat{x} | \phi_m \rangle $;   $a = 1$ ')
plt.xticks(n_values)
plt.yticks(m_values)
plt.xlabel(r'$n$')
plt.ylabel(r'$m$')
plt.grid(False)  # Turn off the grid for cleaner visual
plt.show()
#%%
x = np.linspace(-20,20,1000)
plt.figure()
plt.plot(x, psi(3, x))
plt.plot(x, phi(8, x))
plt.plot(x, psi(n,x) * x * phi(m, x))
plt.grid(True)
plt.show()