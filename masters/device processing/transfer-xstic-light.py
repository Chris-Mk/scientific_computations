from matplotlib.pyplot import *
import pandas as pd

data_light = pd.read_excel('./masters/device processing/files/Transfer_light.xls')
drainI, gateV = -data_light['DrainI'][70:], data_light['GateV'][70:]

grid()
ylabel('-I$_d$ [A]')
xlabel('-V$_d$ [V]')
ticklabel_format(axis="y", style="sci", scilimits=(-3, -3))
plot(gateV, drainI, label='light')

