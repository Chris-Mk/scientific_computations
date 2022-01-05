from matplotlib.pyplot import *
from numpy import *

N = 100
T = linspace(0, 4, N)

P = [4 - t if 2 <= t <= 4 else t for t in T]
plot(T, P, label="func")

pt = 0
a = fft.fft(P) / len(P)
for j in range(1 - N // 2, N // 2):
    A = a[j + N] if j < 0 else a[j]
    pt += A * exp(2j * pi * j * T / 4)

# pt = fft.ifft(a) * len(a)
plot(T, pt, label="Fourier trans")
legend()

err = a[4] - (-1 / (1.5 * pi) ** 2) / (-1 / (1.5 * pi) ** 2)
print(abs(err.real))
