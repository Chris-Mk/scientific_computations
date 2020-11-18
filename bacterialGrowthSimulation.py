import matplotlib.pyplot as plt

# a = [i * (1 - (i / 100)) for i in range(1, 100)]
# b = [j for j in range(1, 100)]

# plt.plot(b, a, 'bo')
# plt.show()

# x_initial = 1
limit = 100
x = []

for k in range(1, limit):
    k_next = k * (1 - (k / limit))
    x.append(k_next)

y = [i for i in range(100)]

plt.xlim(0, 20)
plt.ylim(0, 120)
plt.plot(x)
plt.show()
