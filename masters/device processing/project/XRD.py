from matplotlib.pyplot import *
from numpy import *

# XRD
data_1 = loadtxt('./masters/device processing/project/files/ANP_1.8cm_0.105th_10s.xy')
data_2 = loadtxt('./masters/device processing/project/files/ANP_2.7cm_0.105th_10s.xy')
data_3 = loadtxt('./masters/device processing/project/files/Au0.85Sn0.15.xy')
data_4 = loadtxt('./masters/device processing/project/files/Au0.93Sn0.07.xy')
data_5 = loadtxt('./masters/device processing/project/files/AuSn.xy')
data_6 = loadtxt('./masters/device processing/project/files/Si.xy')
data_7 = loadtxt('./masters/device processing/project/files/SnO.xy')
data_8 = loadtxt('./masters/device processing/project/files/SnO2.xy')
data_9 = loadtxt('./masters/device processing/project/files/Au__fcc.xy')
data_10 = loadtxt('./masters/device processing/project/files/Sn__beta.xy')
data_11 = loadtxt('./masters/device processing/project/files/Sn__diamond.xy')

xlabel('2$\\theta$ [deg]')
ylabel('Intensity [counts]')
plot(data_1[:, 0], data_1[:, 1] / 80, label='1.8 cm tube')
plot(data_2[:, 0], data_2[:, 1] / 100, label='2.7 cm tube')
plot(data_3[:, 0][1900:8000], data_3[:, 1][1900:8000] * 1.2, '--', label='Au0.85Sn0.15')
# plot(data_4[:, 0][1900:8000], data_4[:, 1][1900:8000] * 1.2, '--', label='Au0.93Sn0.07')
plot(data_5[:, 0][1900:8000], data_5[:, 1][1900:8000] * 1.2, '--', label='AuSn')

# plot(data_9[:, 0][1900:8000], data_9[:, 1][1900:8000] * 1.2, '--', label='Au_fcc')

# plot(data_10[:, 0][1900:8000], data_10[:, 1][1900:8000] * 1.2, '--', label='Sn_beta')
# plot(data_11[:, 0][1900:8000], data_11[:, 1][1900:8000] * 1.2, '--', label='Sn_diamond')
#
# plot(data_6[:, 0][1900:8000], data_6[:, 1][1900:8000] * 1.2, '--', label='Si')
# plot(data_7[:, 0][1900:8000], data_7[:, 1][1900:8000] * 1.2, '--', label='SnO')
# plot(data_8[:, 0][1900:8000], data_8[:, 1][1900:8000] * 1.2, '--', label='SnO$_2$')

# plot(data_2[:, 0], data_2[:, 1] / 100, label='2.7 cm tube')
# plot(data_3[:, 0][1900:8000], data_3[:, 1][1900:8000] * 1.2, '--', label='Au0.85Sn0.15')
# plot(data_4[:, 0][1900:8000], data_4[:, 1][1900:8000] * 1.2, '--', label='Au0.93Sn0.07')
# plot(data_5[:, 0][1900:8000], data_5[:, 1][1900:8000] * 1.2, '--', label='AuSn')

# plot(data_9[:, 0][1900:8000], data_9[:, 1][1900:8000] * 1.2, '--', label='Au_fcc')
# plot(data_10[:, 0][1900:8000], data_10[:, 1][1900:8000] * 1.2, '--', label='Sn_beta')
# plot(data_11[:, 0][1900:8000], data_11[:, 1][1900:8000] * 1.2, '--', label='Sn_diamond')

# plot(data_6[:, 0][1900:8000], data_6[:, 1][1900:8000] * 1.2, '--', label='Si')
# plot(data_7[:, 0][1900:8000], data_7[:, 1][1900:8000] * 1.2, '--', label='SnO')
# plot(data_8[:, 0][1900:8000], data_8[:, 1][1900:8000] * 1.2, '--', label='SnO2')
legend()
