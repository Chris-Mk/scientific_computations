from numpy import *

t = linspace(0, 20, 20)
f = sin((pi * t) / 15)
n = len(f)
a = fft.fft(f) / n
q = zeros(n)
z = 1j
for j in arange(-len(a) / 2, (len(f) / 2) - 1):
    x_sums = sum([f[k] * e ** ((2 * pi * z * j * (k - 1)) / n) for k in range(1, n)])
    q[int(n // 2 + j + 1)] = (1 / n) * x_sums

print(q)
