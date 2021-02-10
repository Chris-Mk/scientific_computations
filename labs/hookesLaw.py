from numpy import *
from matplotlib.pyplot import *
import scipy.stats as ss
import pandas as pd

# x = linspace(90, 720, 8)
# y = array([7.2, 6., 5, 6.8, 6.6, 6.4, 6, 5.7])

x = array([92.5, 81, 63.5, 54])
y = array([1.18, .98, 0.75, 0.59])
ylabel('time(s)')
xlabel('circumference(cm)')
title('graph of time(s) vs circumference of balloon(cm)')

slope, intercept, *a = ss.linregress(x, y)
print(f'The gradient is {slope} and y-intercept is {intercept}')
# style.use('seaborn-whitegrid')
# plot(x, y, label="data")
plot(x, x * slope + intercept, label="regression")
legend()
show()
