from matplotlib.pyplot import *
from numpy import *
from scipy.stats import linregress

delays = array([2, 5, 7, 8, 9, 10, 11, 20])
bins = array([44, 122, 174, 200, 226, 252, 278, 459])
m, y_inter, *a = linregress(bins, delays)
exp()

xlabel('bins')
ylabel('Time delay [$\mu s$]')
plot(bins, delays, 'ro')
plot(bins, m * bins + y_inter)
# print(f"{m:.4f} us/bin")
# print(f"{y_inter:.4f} us/bin")
print(m)
print(y_inter)
