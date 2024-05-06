from matplotlib.pyplot import *
from numpy import *
from scipy.constants import *

l = float(input('Quantum well width:')) * 1e-9
v = float(input('Quantum well depth:')) * elementary_charge

# theta = linspace(0, pi, 1000)  # 2.5nm QW
theta = linspace(0, 2 * pi, 1000)  # 10nm QW

lhs, lhs2 = tan(theta), -1 / tan(theta)
lhs[:-1][diff(lhs) < 0] = nan
lhs2[:-1][diff(lhs2) < 0] = nan

# theta_0 = (0.5 * electron_mass * v * l ** 2) / (2 * hbar ** 2) # heavy holes in VB
# theta_0 = (0.082 * electron_mass * v * l ** 2) / (2 * hbar ** 2) # light holes in VB
# rhs = sqrt((0.067 / 0.09024) * (theta_0 / theta ** 2) - 1)  # electrons in sample A
# rhs = sqrt((theta_0 / theta ** 2) - 1)  # electrons in sample A

theta_0 = (0.067 * electron_mass * v * l ** 2) / (2 * hbar ** 2)
# theta_01 = (0.082 * electron_mass * v * l ** 2) / (2 * hbar ** 2)
rhs = sqrt((0.067 / 0.09688) * (theta_0 / theta ** 2 - 1))
# rhs1 = sqrt((0.082 / 0.10188) * (theta_01 / theta ** 2 - 1))

# grid()
ylim(0, 10)
xlabel('$\\theta=\\frac{ka}{2}$')
# gca().xaxis.set_major_formatter(FormatStrFormatter('%g π'))
plot(theta, lhs, label='tan($\\theta$)')
plot(theta, lhs2, label='$-cot(\\theta)$')
plot(theta, rhs, label='$\sqrt{\\frac{\\theta_{0}^2}{\\theta^2}-1}$')
# plot(theta, rhs1, label='$\sqrt{\\frac{\\theta_{0}^2}{\\theta^2}-1}$ for lh')
legend()
# savefig('./masters/graphs/sampleB-electrons energy-levels.pdf')

# intercept = float(input('Theta at the intercept:'))
# energy = (hbar ** 2 * 4 * intercept ** 2) / (2 * 0.082 * electron_mass * l ** 2)
# print(energy / elementary_charge)
