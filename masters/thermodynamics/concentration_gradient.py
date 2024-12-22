from matplotlib.pyplot import *
from numpy import *

x = (linspace(10, 50, 5) * 1e-6) ** 2
c = log(array([83.8, 66.4, 42, 23.6, 8.74]))
fit = polyfit(x, c, 1)
print(fit)

xlabel('$x^2$')
ylabel('$\ln(c)$')
plot(x, c, 'r.')
plot(x, fit[0] * x + fit[1])
savefig('./masters/thermodynamics/files/conc-grad.pdf')
show(block=True)
