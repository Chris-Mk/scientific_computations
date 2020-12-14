from random import shuffle
from numpy import *
from matplotlib.pyplot import *

# names = ["Emma", "Hugo", "Erik", "Josefin", "Mia", "Lukas", "Tim", "Bo"]
#
# # write names to a file
# with open("files/names.txt", "w") as my_file:
#     for name in names:
#         my_file.write(name + " ")
#
# # my_file.close()
#
# # read names from a file and prints
# my_file = open("files/names.txt")
# var = [name for name in my_file.read().split(" ") if name != ""]
# print(var)
# shuffle(var)
# print(var)
# # print(my_file.read())
# my_file.close()
#
# # numpy array
# arr1 = array([1, 2, 3])
# arr2 = array([4, 5, 6])
#
# savetxt("files/array.txt", arr1)
# print(loadtxt("files/array.txt"))
# save("files/array", arr1)
# print(load("files/array.npy"))

# Task 01
mapper = {}
with open("files/kwh.dat") as myFile:
    for line in myFile.readlines():
        k, v = line.split()
        mapper[k] = int(v)

# Task 02
mapper = dict(sorted(mapper.items(), key=lambda kvp: kvp[0]))
# print(mapper)

# Task 05
mapper = {v: k for k, v in mapper.items()}
print("Month with lowest energy consumption is", mapper[min(mapper.keys())])
print("Month with highest energy consumption is", mapper[max(mapper.keys())])
# print(mapper)

# Task 06
kwh = array(list(mapper.keys()))
max_consump = -inf
min_consump = inf
max_index = min_index = -1

for i in range(len(kwh) - 1):
    diff = abs(kwh[i] - kwh[i + 1])
    if max_consump < diff:
        max_consump = diff
        max_index = i + 1
    elif min_consump > diff:
        min_consump = diff
        min_index = i + 1

print(max_index, min_index)
print(mapper.get(kwh[max_index]))
print(mapper.get(kwh[min_index]))

# Task 07
print(f'Average kwh = {sum(list(mapper.keys())) / len(mapper.keys()):0.2f}')


# Task 08
x = linspace(-5, 5, 100)
y1 = vectorize(lambda j: j ** 3 + sin(j))(x)
y2 = vectorize(lambda j: 3 * j ** 2 + cos(j))(x)

plot(x, y1)
plot(x, y2)
show()
