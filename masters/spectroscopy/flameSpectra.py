from matplotlib.pyplot import *
from numpy import *
from pandas import *

# data = loadtxt('./masters/spectroscopy/files/400ms10avg.xlsx', skiprows=6)
data = read_excel('./masters/spectroscopy/files/400ms10avg.xlsx', skiprows=6)
# plot(data[0], data[1])
print(data[0])
