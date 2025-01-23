from matplotlib.pyplot import *
from numpy import *
import scipy.constants as sc

t1 = 1 / (273 + array([325, 350, 375]))
k1 = log(array([4.57, 6.73, 11.78]))
fit1 = polyfit(t1, k1, 1)
print(-fit1 * sc.gas_constant)

t2 = 1 / (273 + array([490, 500, 525]))
k2 = log(array([3.43, 7.23, 16.7]))
fit2 = polyfit(t2, k2, 1)
print(-fit2 * sc.gas_constant)

# grid()
# xlabel('1/T [1/K]')
# ylabel('$\ln(k)$ [nm/s]')
# plot(t1, k1, 'r.')
# plot(t1, fit1[0] * t1 + fit1[1])
# savefig('./masters/thermodynamics/files/Ea1.pdf')
# show(block=True)

grid()
xlabel('1/T [1/K]')
ylabel('$\ln(k)$ [nm/s]')
plot(t2, k2, 'r.')
plot(t2, fit2[0] * t2 + fit2[1])
# savefig('./masters/thermodynamics/files/Ea2.pdf')
show(block=True)
