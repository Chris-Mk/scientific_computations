x_initial = 1
fraction_sum = 0


def f(x):
    if x >= 1:
        x = 1 + (1 / f(x))
    return x


fraction_sum += f(x_initial)

# for i in range(1, 100):
#     x = 1 + (1 / x)
#
# print(fraction_sum)


# print(array)

# curr_x = 1
# root_sum = 0
#
# for j in range(100):
#     root_sum += np.sqrt(curr_x)
#     curr_x = root_sum
