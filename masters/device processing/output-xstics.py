from matplotlib.pyplot import *
import pandas as pd

data = pd.read_excel('./masters/device processing/files/Output_dark.xls')
drainI1, drainV1, gateV1 = -data['DrainI(1)'] * 1000, -data['DrainV(1)'], data['GateV(1)']
drainI2, drainV2, gateV2 = -data['DrainI(2)'] * 1000, -data['DrainV(2)'], data['GateV(2)']
drainI3, drainV3, gateV3 = -data['DrainI(3)'] * 1000, -data['DrainV(3)'], data['GateV(3)']
drainI4, drainV4, gateV4 = -data['DrainI(4)'] * 1000, -data['DrainV(4)'], data['GateV(4)']
drainI5, drainV5, gateV5 = -data['DrainI(5)'] * 1000, -data['DrainV(5)'], data['GateV(5)']
drainI6, drainV6, gateV6 = -data['DrainI(6)'] * 1000, -data['DrainV(6)'], data['GateV(6)']
drainI7, drainV7, gateV7 = -data['DrainI(7)'] * 1000, -data['DrainV(7)'], data['GateV(7)']

grid()
title('Output Characteristic of MOSFET')
ylabel('-I$_d$ [mA]')
xlabel('-V$_d$ [V]')
# ticklabel_format(axis="y", style="sci", scilimits=(-3, -3))
plot(drainV1, drainI1, label='V$_G$=-3V')
plot(drainV2, drainI2, label='V$_G$=-2V')
plot(drainV3, drainI3, label='V$_G$=-1V')
plot(drainV4, drainI4, label='V$_G$=0V')
plot(drainV5, drainI5, label='V$_G$=1V')
plot(drainV6, drainI6, label='V$_G$=2V')
plot(drainV7, drainI7, label='V$_G$=3V')
legend()
show(block=True)

# savefig('./masters/graphs/output-xstics.pdf')
