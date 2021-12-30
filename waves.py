import matplotlib.pyplot as plt
from numpy import *
from scipy.integrate import quad
from sympy import DiracDelta


def a(k):
    return (2 * pi * 5 * DiracDelta(k)) + (4 * pi * 0.1) / (
            25 * ((k - ((2 * pi) / 5) ** 2) + ((2 * pi) / 25) ** 2))


def integrand(k, x, t):
    return a(k) * cos(k * x - sqrt(9.81 * 0.15) * abs(k) * t)


x_range = linspace(-50, 50, 100)
h_range = zeros(len(x_range))

for i in range(len(x_range)):
    h_range[i] = (1 / (2 * pi)) * quad(integrand, -inf, inf, args=(x_range[i], 0))[0]

plt.grid()
plt.xlabel("x")
plt.ylabel("h(x, 0)")
plt.plot(x_range, h_range, label="t=0")
plt.legend()

# for t in t_range:
#     h_range = zeros(len(x_range))
#     for i in range(len(x_range)):
#         h_range[i] = (1 / (2 * pi)) * quad(integrand, -inf, inf, args=(x_range[i], t))[0]
#     print("t = ", t)
#     plt.grid()
#     plt.plot(x_range, h_range, label=f"t={t}")
#     plt.legend()
