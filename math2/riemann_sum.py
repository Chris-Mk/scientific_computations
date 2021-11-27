from numpy import *
from scipy.integrate import quad


def func1(t):
    return t ** 2
    # return (1 - t ** 2) ** 0.5


def func2(t):
    return (9 * t ** 4 + 4 * t ** 2) ** 0.5


def rie_sum(f, a, b, n):
    width = (b - a) / n

    x = linspace(a, b, n + 1)
    mid_x = [(x[i] + x[i + 1]) / 2 for i in range(0, len(x) - 1)]
    mid_y = [f(i) * width for i in mid_x]

    upper_y = [f(i) * width for i in x]
    lower_y = [f(x[i]) * width for i in range(1, len(x))]

    return sum(mid_y), sum(upper_y), sum(lower_y)


mid_sum, upper_sum, lower_sum = rie_sum(func1, 0, 1, 1000)
print(f'Upper sum = {upper_sum}\nMid sum = {mid_sum}\nLower sum = {lower_sum}')

integration = quad(func1, 0, 1)[0]
print("Integration = ", integration)

print("Difference =", abs(integration - mid_sum))
