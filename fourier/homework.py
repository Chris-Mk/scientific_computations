from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import quad

N = 7
T = ((4 * pi ** 2) / 30)
a0 = (1 / T) * quad(lambda t: sin((30 * t) / T), 0, T)[0]
aj = (2 / T) * array([quad(lambda t: sin((30 * t) / T) * cos((2 * pi * j * t) / T), 0, T)[0] for j in range(1, N)])
bk = (2 / T) * array([quad(lambda t: sin((30 * t) / T) * sin((2 * pi * k * t) / T), 0, T)[0] for k in range(1, N)])

print(a0)
print(len(aj))
print(len(bk))


def p(t, n):
    return a0 + sum([aj * cos((2 * pi * j * t) / T) for j in range(1, n)]) + sum(
        [bk * sin((2 * pi * j * t) / T) for j in range(1, n)])


x = linspace(0, 2 * pi, 1000)

# for count in range(1, N + 1):
#     y = [p(i, count) for i in x]
#
#     plot(x, y, label=f"N = {count}")
#     grid()
#     legend()

y = [p(i, N) for i in x]

title("Estimate number of coefficients = 13")
grid()
plot(x, y)
