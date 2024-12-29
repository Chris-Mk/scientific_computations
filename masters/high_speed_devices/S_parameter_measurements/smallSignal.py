from matplotlib.pyplot import *
from numpy import *
import pandas as pd

from masters.high_speed_devices.S_parameter_measurements import s2ny, s2nz, nz2s, ny2s

off_data = array(pd.read_csv('./masters/high_speed_devices/S_parameter_measurements/files/Group1/A04_off.csv', header=None))
# on_data = array(pd.read_csv('./masters/high_speed_devices/S_parameter_measurements/files/Group1/A04_on.csv', header=None))

Z0 = 50
Rs = Rg = Rd = 2  # Defining the external resistances
Z = array([Rs + Rg, Rs, Rs, Rs + Rd])  # Z-parameter matrix for external resistances
nz = array([s2nz.s2nz(i) for i in off_data]) / Z0  # Normalized z-parameters from the data

freq = nz[:, 4:].real.flatten() * 2 * pi * Z0 # angular frequency
# Normalized z-parameter for each element in the z-parameter matrix minus respective external resistances
# (Z_removed = Z_measured - Z_ext_resistances)
nz11 = nz[:, 0:1].flatten() - Z[0]
nz21 = nz[:, 1:2].flatten() - Z[1]
nz12 = nz[:, 2:3].flatten() - Z[2]
nz22 = nz[:, 3:4].flatten() - Z[3]

# Method from wikipedia (https://en.wikipedia.org/wiki/Admittance_parameters#Relation_to_Z-parameters)
z_magnitude = nz11 * nz22 - nz21 * nz12
ny11 = nz22 / z_magnitude
ny21 = -nz21 / z_magnitude
ny12 = -nz12 / z_magnitude
ny22 = nz11 / z_magnitude

# Alternative to getting normalized y-parameters (my own reasoning and understanding)
# s-parameters obtained from the above normalized z-parameters
# s11 = nz2s.nz2s(nz11)
# s21 = nz2s.nz2s(nz21)
# s12 = nz2s.nz2s(nz12)
# s22 = nz2s.nz2s(nz22)
#
# # normalized y-parameters obtained from the above s-parameters
# ny11 = s2ny.s2ny(s11)
# ny21 = s2ny.s2ny(s21)
# ny12 = s2ny.s2ny(s12)
# ny22 = s2ny.s2ny(s22)

fit11 = polyfit(freq, ny11, 1)

fit21 = polyfit(freq, ny21, 1)
fit12 = polyfit(freq, ny12, 1)
fit22 = polyfit(freq, ny22, 1)

xscale('log')
xlabel('$\omega$')
ylabel('$Y$')

plot(freq[220:], ny11[220:].real, label='ny11 real')
plot(freq[220:], ny21[220:].real, label='ny21 real')
plot(freq[220:], ny12[220:].real, label='ny12 real')
plot(freq[220:], ny22[220:].real, label='ny22 real')

# plot(freq[220:], ny11[220:].imag, label='ny11')
# plot(freq[220:], ny21[220:].imag, label='ny21')
# plot(freq[220:], ny12[220:].imag, label='ny12')
# plot(freq[220:], ny22[220:].imag, label='ny22')
#
# plot(freq[220:], fit11[0].real * freq[220:] + fit11[1].real, label='fit11')
# plot(freq[220:], fit21[0].real * freq[220:] + fit21[1].real, label='fit12')
# plot(freq[220:], fit12[0].real * freq[220:] + fit12[1].real, label='fit21')
# plot(freq[220:], fit22[0].real * freq[220:] + fit22[1].real, label='fit22')

# plot(freq[220:], ny11[220:].imag / freq[220:], label='Cgg')
# plot(freq[220:], -ny12[220:].imag / freq[220:], label='Cgd')
# plot(freq[220:], ny12[220:].imag + ny22[220:].imag / freq[220:], label='Cdb')

legend()
show(block=True)
