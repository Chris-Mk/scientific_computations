from matplotlib.pyplot import *
from numpy import *


def p(t, n):
    return (4 / pi) * sum([(sin(2 * pi * (2 * j + 1) * (t / 2))) / (2 * j + 1) for j in range(n)])


N = 10
x = linspace(0, 2 * pi, 1000)

# for count in range(1, N):
#     y = [p(i, count) for i in x]
#
#     plot(x, y, label=f"N = {count}")
#     grid()
#     legend()

y = [p(i, N) for i in x]
grid()
plot(x, y)
