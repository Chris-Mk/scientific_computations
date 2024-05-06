from matplotlib.pyplot import *
from numpy import *

E1, E2, E3, tau, beta, hbar, kb = 0, 1, 2, 2, 2, 1, 1
t = linspace(0.001, 1, 10)  # timescale for 2 states system
# t = linspace(0.1, 1, 500)  # timescale for 3 states system
f = zeros(len(t))
step = t[1] - t[0]
f[0] = f[1] = 0.5  # for two states system

# Initial values of f for the three states system
# f[0] = f[1] = 0
# f[2] = 1

# Defining W_{i->j}
omega12 = 1 / (exp((E2 - E1) * beta) - 1)
omega21 = (1 / (exp((E2 - E1) * beta) - 1) + 1)
omega23 = (1 / (exp(2 * (E3 - E2) * beta) - 1))
omega32 = (1 / (exp(2 * (E3 - E2) * beta) - 1) + 1)

# For 2 states system
index = 0
for i in range(2, len(t)):
    f_next = f[index] + t[index] * (omega21 * f[index + 1] * (1 - f[index]) - omega12 * f[index] * (1 - f[index + 1]))
    f[i] = f_next
    index += 1

# For 3 states system
# index = 0
# for i in range(3, len(t)):
#     f_next = f[index] + t[index] * ((omega21 * f[index + 1] * (1 - f[index]) - omega12 * f[index] * (1 - f[index + 1]))
#                                     + (omega32 * f[index + 2] * (1 - f[index + 1]) - omega23 * f[index + 1] * (1 - f[index + 2])))
#     f[i] = f_next
#     index += 1

xlabel('t')
ylabel('f')
plot(t, f, label="$\Delta t=$" + round(step, 3).astype(str))
legend()
