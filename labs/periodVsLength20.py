from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

length = linspace(15, 90, 6) / 100
period = array([0.62, 0.90, 1.49, 2.10, 2.66, 3.02])
slope, y_inter, _r, _p, _s = sp.linregress(length, period)

print(f'The slope is {slope} and y-intercept is {y_inter}')
xlabel('length[m]')
ylabel('period[$s^2$]')
title('graph of length vs period')
grid()
plot(length, period, 'bo', label='data')
plot(length, length * slope + y_inter, label='linear regression')
legend()

g = (4 * pi ** 2) / slope
print(f'Gravitational acceleration on Earth is {g}')
print(f'Standard deviation is {_s} of the slope')
