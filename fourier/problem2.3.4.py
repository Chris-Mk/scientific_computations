from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import quad

a0 = 0.5 * quad(lambda t: (t / 4), 0, 2)[0]
aj = array([quad(lambda t: (t / 4) * cos(pi * j * t), 0, 2)[0] for j in range(1, 25)])
bk = array([quad(lambda t: (t / 4) * sin(pi * k * t), 0, 2)[0] for k in range(1, 25)])


def p(t, n):
    return a0 + sum([aj * cos(pi * j * t) for j in range(1, n)]) + sum(
        [bk * sin(pi * j * t) for j in range(1, n)])


N = 25
x = linspace(0, 2 * pi, 1000)

# for count in range(1, N + 1):
#     y = [p(i, count) for i in x]
#
#     plot(x, y, label=f"N = {count}")
#     grid()
#     legend()

y = [p(i, N) for i in x]
grid()
plot(x, y)
