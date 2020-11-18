import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# task 01
# =============================================================================

# my_list = [0, 1, 2, 1, 0, -1, -2, -1, 0]


# print(my_list[0])
# print(my_list[-1])
# print(my_list[:-1])
# print(my_list[1:-1])
# print(my_list + my_list[1:-1] + my_list)
# print(my_list)
# my_list[2] = 8
# print(my_list)
# my_list[2:2] = [-3]
# print(my_list)
# my_list[3:4] = []
# print(my_list)
# my_list[2:5] = [-5]
# print(my_list)


# =============================================================================
# task 02
# =============================================================================

# def f1(x):
#     return np.sin(x)
#
#
# print(f1(3))
# print(f1(2 * np.pi))


# =============================================================================
# task 03
# =============================================================================

# def f2(m):
#     var_list = [n - m // 2 for n in range(m)]
#     print(var_list)
#     return 1 + var_list[0] + var_list[-1]
#
#
# print(f2(2))

# =============================================================================
# task 04
# =============================================================================

# distance = [
#     [0, 20, 30, 40],
#     [20, 0, 50, 60],
#     [30, 50, 0, 70],
#     [40, 60, 70, 0]
# ]
#
# rd = []
# for i in range(1, len(distance)):
#     rd.append(distance[i][:i])
#
# print(rd)
#
# print([distance[i][:i] for i in range(1, len(distance))])
#
# red_distance = [
#     [distance[0][1]],
#     distance[2][0:2],
#     distance[3][0:3]
# ]
#
# print(red_distance)


# =============================================================================
# task 05
# =============================================================================

# def f3(a, b):
#     return (a - b).union(b - a)
#
#
# print(f3({1, 2}, {2, 3}))
# print({1, 2}.symmetric_difference({2, 3}))


# =============================================================================
# task 06
# =============================================================================

# my_set = {4, 5, 6}
# print(my_set.intersection({2, 3, 4}))
# print(my_set.intersection_update({2, 3, 4}))

# =============================================================================
# task 07
# =============================================================================

def f4(func, a, b, tol):
    if np.sign(a) == np.sign(b):
        return "The interval (a,b) must be opposite signs!"

    while True:
        mid = (a + b) / 2

        if np.sign(func(a)) != np.sign(func(mid)):
            b = mid
        else:
            a = mid

        if np.abs(a - b) < tol:
            return (a + b) / 2, a, b


i, j, k = f4(lambda x: x ** 2 - 4, -1, 1, 1.e-8)
print(f"mid-point = {k}\na = {j}\nb ={k}")
