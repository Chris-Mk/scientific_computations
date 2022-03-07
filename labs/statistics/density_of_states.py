from matplotlib.pyplot import *
from numpy import *

T = linspace(0.1, 1, 1000)
E = flip(array(range(-13, 1, 1)))
g = flip(array([1, 0, 86, 645, 9046, 77535, 710407, 5824861, 40339545,
                234326487, 1222946058, 5351538782, 15687265041, 18671059783.5]))


def heat_capacity(temp):
    return (exp_value(temp, 2) - exp_value(temp, 1) ** 2) / temp ** 2


def exp_value(temp, power):
    numerator = sum([(E[i] ** power) * g[i] * exp(-(E[i] - E[-1]) / temp) for i in range(E.size)])
    denominator = sum([g[i] * exp(-(E[i] - E[-1]) / temp) for i in range(E.size)])
    return numerator / denominator


def p_native(temp):
    numerator = 1
    denominator = sum([g[i] * exp(-(E[i] - E[-1]) / temp) for i in range(E.size)])
    return numerator / denominator


xlabel('T')
grid()

# Plotting Cv vs T
ylabel('$C_v$')
plot(T, [heat_capacity(t) for t in T])

# Plotting P_nat vs T
# ylabel('$P_{nat}$')
# plot(T, [p_native(t) for t in T])

# savefig('./graphs/P_nat-temp.pdf')
