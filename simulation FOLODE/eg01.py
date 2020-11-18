import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 9)
y = np.linspace(-2, 2, 9)

print(x)
print(y)
derivative = []
for i in y:
    for j in x:
        if j == 0:
            continue
        plt.plot(i / j)
        plt.show()
        # derivative.append(i / j)

# print(derivative)

# plt.plot(x, y)
# plt.ylim(-2, 2)
# plt.xlim(-2, 2)
plt.show()
