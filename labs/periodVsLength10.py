from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

length = linspace(15, 90, 6) / 100
period = array([0.61, 1.20, 1.81, 2.41, 3.01, 3.60])
slope, y_inter, *a = sp.linregress(length, period)

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
print(f'Standard deviation is {a[2]} of the slope')
