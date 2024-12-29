from matplotlib.pyplot import *
from numpy import *
import pandas as pd

from masters.high_speed_devices.S_parameter_measurements import s2ny, s2nz, nz2s, ny2s

off_data = array(pd.read_csv('C:/Users/LENOVO/PycharmProjects/scientific_computations/masters'
                             '/high_speed_devices/S_parameter_measurements/files/Group1/A04_off.csv', header=None))
on_data = array(pd.read_csv('C:/Users/LENOVO/PycharmProjects/scientific_computations/masters'
                            '/high_speed_devices/S_parameter_measurements/files/Group1/A04_on.csv', header=None))

Z0 = 50
Rs = Rg = Rd = 2  # Defining the external resistances
Z = array([Rs + Rg, Rs, Rs, Rs + Rd])  # Z-parameter matrix for external resistances
nz = array([s2nz.s2nz(i).real for i in off_data]) / Z0  # Normalized z-parameters from the data

freq = nz[:, 4:].flatten() * 2 * pi * Z0
# Normalized z-parameter for each element in the z-parameter matrix minus respective external resistances
# (Z_removed = Z_measured - Z_ext_resistances)
nz11 = nz[:, 0:1].flatten() - Z[0]
nz21 = nz[:, 1:2].flatten() - Z[1]
nz12 = nz[:, 2:3].flatten() - Z[2]
nz22 = nz[:, 3:4].flatten() - Z[3]

z_mod = nz11 * nz22 - nz21 * nz12

ny11 = nz22 / z_mod
ny21 = -nz21 / z_mod
ny12 = -nz12 / z_mod
ny22 = nz11 / z_mod

# s-parameters obtained from the above normalized z-parameters
# s11 = nz2s.nz2s(nz11)
# s21 = nz2s.nz2s(nz21)
# s12 = nz2s.nz2s(nz12)
# s22 = nz2s.nz2s(nz22)
#
# # normalized y-parameters obtained from the above s-parameters
# ny11 = s2ny.s2ny(s11).real
# ny21 = s2ny.s2ny(s21).real
# ny12 = s2ny.s2ny(s12).real
# ny22 = s2ny.s2ny(s22).real

xscale('log')
xlabel('$\omega$')
ylabel('$Y$')
# plot(freq[220:], nz11[220:])
plot(freq[220:], ny11[220:], label='ny11')
plot(freq[220:], ny22[220:], label='ny22')
plot(freq[220:], ny12[220:], label='ny12')
plot(freq[220:], ny21[220:], label='ny21')
legend()
show()

# ny = array([s2ny.s2ny(i) for i in data])
# sz = array([nz2s.nz2s(i) for i in data])
# sy = array([ny2s.ny2s(i) for i in data])

# print(ny)
# print(sz)
# print(sy)
