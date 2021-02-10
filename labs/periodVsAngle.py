from numpy import *
from matplotlib.pyplot import *
import scipy.stats as sp

angles = linspace(10, 30, 5)
period = array([17.31, 17.34, 17.37, 17.45, 17.50])
# sp.linregress(angles, period)

grid()
xlabel('amplitude[degree]')
ylabel('time period[$s$]')
title('graph of period vs angle of elevation')
plot(angles, period, label='data')
legend()
