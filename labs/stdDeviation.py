from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

d15 = array([15.51, 15.56, 15.61, 15.76, 15.74])
d30 = array([21.92, 21.77, 21.89, 21.93, 21.82])
d45 = array([26.94, 26.85, 26.89, 26.91, 26.85])
d60 = array([31.02, 31.01, 31.12, 30.99, 31.07])
d75 = array([34.92, 34.70, 34.56, 34.72, 34.67])
d90 = array([37.68, 38.19, 37.88, 37.99, 38.05])

stds = array([std(d15), std(d30), std(d45), std(d60), std(d75), std(d90)])

print(average(stds) / sqrt(len(stds)))

period = array([0.61, 1.20, 1.81, 2.41, 3.01, 3.60])
print(std(period) / sqrt(len(period)))
