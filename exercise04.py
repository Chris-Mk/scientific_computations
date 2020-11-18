import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# task 01 - complex valued function
# =============================================================================

def f(x, r):
    x = np.deg2rad(x)
    re = r * np.cos(x)
    img = r * np.sin(x)
    return complex(re, img)


real = []
imaginary = []
for j in np.arange(0.1, 1.1, 0.1):
    for i in range(360):
        z = f(i, j)
        a = z.real
        b = z.imag

        real.append(a)
        imaginary.append(b)

plt.plot(real, imaginary)
plt.show()


# =============================================================================
# task 02
# =============================================================================

def newton(func, fp, x, tol=1e-8):
    is_conv = False

    for counter in range(400):
        x_next = x - (func(x) / fp(x))

        if np.abs(x - x_next) < tol:
            is_conv = True
            break
        x = x_next
    return is_conv, x


conv, val = newton(lambda x: x ** 2 + 3 * x + 2,
                   lambda x: 2 * x + 3,
                   1)

print(f"Converges? {conv}. At {val}")
