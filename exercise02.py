import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# task 01
# =============================================================================

x = 0.5
a = 0.5
x_array = []
counter = 0

for i in range(200):
    x_new = np.sin(x) - a * x + 30

    if abs(x - x_new) < 1e-8:
        print("x - x_new is less than 1.e-8!")
        break
    x_array.append(x)
    counter = i
    x = x_new

print(f'The result after {counter} iterations is {x}')

# =============================================================================
# task 02
# =============================================================================

y = np.linspace(5, 31, len(x_array))
plt.plot(x_array, y, label="y=g(x)", color="brown")
plt.plot(x_array, x_array, label="y=x", color="red")
plt.legend()
# plt.show()

# =============================================================================
# task 03
# =============================================================================

xn = []
n = 1

while True:
    if xn and xn[-1] < 1e-9:
        break

    xn.append((np.sin(n) ** 2) / n)
    n += 1

print(len(xn))
print(n)

count = 1
while True:
    x = (np.sin(count) ** 2) / count

    if x < 1.e-9:
        break

    count += 1
print(count)

# =============================================================================
# task 04
# =============================================================================

x = 1
alpha = .5
counter = 0
negativeElements = []
positiveElements = []

while True:
    x_new = 0.2 * x - alpha * (x ** 2 - 5)
    counter += 1

    if x_new < 0:
        negativeElements.append(x_new)
        # print("Negative element detected!")
    else:
        positiveElements.append(x_new)

    if counter >= 500:
        break

    if np.abs(x - x_new) < 1.e-9:
        print(f"Sequence converged to x = {x_new}")
        break

    x = x_new

if counter >= 500:
    print("No convergence detected!")

print("Negative elements count: ", len(negativeElements))
print("Positive elements count: ", len(positiveElements))


# Alternative way
# for count in range(500):
#     x_new = 0.2 * x - alpha * (x ** 2 - 5)
#
#     if x_new < 0:
#         print("Negative element detected!")
#
#     if np.abs(x - x_new) < 1.e-9:
#         print(f"Sequence converged to x = {x_new}")
#         break
#     x = x_new

# =============================================================================
# task 04
# =============================================================================


def f(beta):
    x_prev = 1

    for index in range(31):
        x_prime = 0.2 * x_prev - beta * (x_prev ** 2 - 5)

        if np.abs(x_prev - x_prime) < 1e-9:
            return True
        x_prev = x_prime
    return False


print("Does it converge? :", f(.5))
print("Does it converge? :", f(-.5))
print("Does it converge? :", f(.25))
print("Does it converge? :", f(-.25))
# print(f(1))
