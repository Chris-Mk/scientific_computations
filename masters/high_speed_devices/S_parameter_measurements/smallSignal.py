from matplotlib.pyplot import *
from numpy import *
import pandas as pd

from masters.high_speed_devices.S_parameter_measurements import s2ny, s2nz, nz2s, ny2s

# off_data = array(pd.read_csv('C:/Users/LENOVO/PycharmProjects/scientific_computations/masters'
#                              '/high_speed_devices/S_parameter_measurements/files/Group4/C04_off.csv', header=None))
on_data = array(pd.read_csv('C:/Users/LENOVO/PycharmProjects/scientific_computations'
                            '/masters/high_speed_devices/S_parameter_measurements/files/Group4/C04_on.csv', header=None))

Z0 = 50
Rs = Rg = Rd = 2  # Defining the external resistances
Z = array([Rs + Rg, Rs, Rs, Rs + Rd])  # Z-parameter matrix for external resistances
nz = array([s2nz.s2nz(i) for i in on_data]) / Z0  # Normalized z-parameters from the data

freq = nz[:, 4:].real.flatten() * Z0  # angular frequency
# Normalized z-parameter for each element in the z-parameter matrix minus respective external resistances
# (Z_removed = Z_measured - Z_ext_resistances)
nz11 = nz[:, 0:1].flatten() - Z[0]
nz21 = nz[:, 1:2].flatten() - Z[1]
nz12 = nz[:, 2:3].flatten() - Z[2]
nz22 = nz[:, 3:4].flatten() - Z[3]

# Method from wikipedia (https://en.wikipedia.org/wiki/Admittance_parameters#Relation_to_Z-parameters)
# Converting z to y parameters
z_magnitude = (nz11 * nz22) - (nz21 * nz12)
ny11 = nz22 / z_magnitude
ny21 = -nz21 / z_magnitude
ny12 = -nz12 / z_magnitude
ny22 = nz11 / z_magnitude

xscale('log')
xlabel('freq [GHz]')
# ylabel('Im(Y) [$\Omega^{-1}$]')
# plot(freq[220:], ny11[220:].imag, label='Im(ny11)')
# plot(freq[220:], ny21[220:].imag, label='Im(ny21)')
# plot(freq[220:], ny12[220:].imag, label='Im(ny12)')
# plot(freq[220:], ny22[220:].imag, label='Im(ny22)')

# ylabel('C [F]')
# plot(freq[220:], ny11[220:].imag / freq[220:], label='$C_{gg}$')
# plot(freq[220:], -ny12[220:].imag / freq[220:], label='$C_{gd}$')
# plot(freq[220:], ny22[220:].imag / freq[220:], label='$C_{gd} + C_{sd}$')

h21 = ny21 / ny11
k = (2 * ny11.real * ny22.real - (ny12 * ny21).real) / abs(ny12 * ny21)
MSG = abs(ny21 / ny12)
MAG = MSG * (k - sqrt(k ** 2 - 1))
U = abs(ny21 - ny12) ** 2 / (4 * (ny11.real * ny22.real - ny12.real * ny21.real))

ylabel('Gain [dB]')
plot(freq[150:], 20 * log10(abs(h21[150:])), label='$h_{21}$')
plot(freq[150:], 10 * log10(k[150:]), label='k')
plot(freq[150:], 10 * log10(abs(MSG[150:])), label='MSG')
plot(freq[150:], 10 * log10(MAG[150:]), label='MAG')
plot(freq[150:], 10 * log10(U[150:]), label='U')

legend()
show(block=True)
