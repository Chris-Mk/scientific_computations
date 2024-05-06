from matplotlib.pyplot import *
import scipy.stats as sp
import pandas as pd

data_dark = pd.read_excel('./masters/device processing/files/Transfer_dark.xls')
data_light = pd.read_excel('./masters/device processing/files/Transfer_light.xls')
drainI, gateV = -data_dark['DrainI'][68:] * 1000, data_dark['GateV'][68:]
drainI2, gateV2 = -data_light['DrainI'][68:] * 1000, data_light['GateV'][68:]

slope, y_inter, *a = sp.linregress(data_dark['GateV'][70: 73], -data_dark['DrainI'][70: 73] * 1000)
slope2, y_inter2, *a2 = sp.linregress(data_light['GateV'][70: 73], -data_light['DrainI'][70: 73] * 1000)
print("Transconductance in dark = ", slope)
print("Transconductance in light = ", slope2)

subplot(121)
grid()
title('Transfer Characteristic in Dark')
ylabel('-I$_d$ [mA]')
xlabel('-V$_g$ [V]')
text(0.48, 0, 'V$_T$ = 0.478V', size=12)
# ticklabel_format(axis="y", style="sci", scilimits=(-3, -3))
plot(gateV, drainI)
plot(gateV[7: 24], slope * gateV[7: 24] + y_inter, 'r--', label='linear regression')
legend()

subplot(122)
grid()
title('Transfer Characteristic in Light')
# ylabel('-I$_d$ [A]')
xlabel('-V$_g$ [V]')
text(0.48, 0, 'V$_T$ = 0.499V', size=12)
# ticklabel_format(axis="y", style="sci", scilimits=(-3, -3))
plot(gateV2, drainI2)
plot(gateV2[7: 24], slope2 * gateV2[7: 24] + y_inter2, 'r--', label='linear regression')
legend()
