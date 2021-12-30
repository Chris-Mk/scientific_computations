from numpy import *
from matplotlib.pyplot import *

t = linspace(0, 2 * pi, 200)
f = sin((30 * t) / (2 * pi))
n = len(f)
a = fft.fft(f) / n
# pt = zeros(n)
# z = 1j
# for j in arange(-len(a) / 2, (len(f) / 2) - 1):
#     x_sums = sum([f[k] * e ** ((2 * pi * z * j * (k - 1)) / n) for k in range(1, n)])
#     pt[int(n // 2 + j + 1)] = (1 / n) * x_sums

q = []
for ti in t:
    for j in arange((1 - n) / 2, (n / 2) - 1):
        j = int(j)
        q.append(a[j] * e ** ((2j * pi * j * ti) / (2 * pi)))

# x_sums = sum( for k in range(1, n)])
# pt[int(n // 2 + j + 1)] = (1 / n) * x_sums

# print(array(q))
grid()
plot(t, array(q))
