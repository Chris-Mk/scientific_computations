from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import quad
from scipy.optimize import fsolve, bisect

delta0 = 4.164630809100345e-7
kbT = array([.1, .2, .3, .4, .5, .56]) * delta0


def integrand(energy, delta, kT):
    return tanh(sqrt(delta ** 2 + energy ** 2) / (2 * kT)) / sqrt(delta ** 2 + energy ** 2)
    # return 1 / sqrt(delta ** 2 + energy ** 2)


def gap(delta, kT):
    return quad(integrand, -1, 1, args=(delta, kT))[0]


# delta2 = 1 / sinh(2 / 0.13)
# print(delta2)
delta3 = 2 * exp(-2 / 0.1)
print(delta3)
delta1 = bisect(lambda delta: (0.1 / 4) * gap(delta, 0) - 1, 0, 1)
print(delta1)
# print(gap(delta0, 0))


x = y = []
for i in kbT:
    _ = bisect(lambda delta: (0.1 / 4) * gap(delta, i) - 1, 0, 1)
    x.append(gap(_, i))
    y.append(_)

xlabel('log$_{10} \Delta$')
semilogx(x, y)

print('Diff 1=', abs(delta1 - delta3))
# print('Diff 1=', delta1 - delta2)
# print('Diff 2=', delta2 - delta3)
