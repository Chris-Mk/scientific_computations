from matplotlib.pyplot import *
import pandas as pd
from scipy.stats import linregress

data = pd.read_csv("./thesis/data/electrical_measurements/data LOG_42.txt", "\t", header=1,
                   names=["Time(s):", "Sweep V(V):", "Ch1 I1(A):", "Ch1 I2(A):", "Ch2 V1(V):", "Ch2 V2(V):"])

I = (data["Ch1 I1(A):"] + data["Ch1 I2(A):"]) / 200
V = (data["Ch2 V1(V):"] + data["Ch2 V2(V):"]) / 0.2
m, y_inter, *a = linregress(I, V)
print("Resistance: ", m - 100)

grid()
xlabel("I [A]")
ylabel("V [V]")
title("Four-probe measurement")
ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
text(-2e-9, 4e-3, f"Resistance={(m / 1000)- 100:.0f}$\Omega$", fontsize=12)
plot(I, V, "ro")
plot(I, m * I + y_inter)
legend()

# Log22
# Gap1
# 4T Keithley
#
# SOURCE A1: V (DC) smuA K2636
#  (Start:Stop:Step:Div) : (-0.025 : 0.025 : 0.001 : 1)
# Ch1 Amplifier (x/V): 1.000E-6
# Ch2 Amplifier (x/V): 200.000E-3
# Average resistance: 39.4703E+3


# Log23 - preferred over log22
# Gap1
# 4T Keithley
#
# SOURCE A1: V (DC) smuA K2636
#  (Start:Stop:Step:Div) : (-0.025 : 0.025 : 0.001 : 1)
# Ch1 Amplifier (x/V): 10.000E-6
# Ch2 Amplifier (x/V): 200.000E-3
# Average resistance: 20.8977E+3


# Log42
# Gap3
# 4-12
# 4 probe femto
# After pumping overnight
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Ch2 Amplifier (x/V): 10.000E-3
# Average resistance: 3.7875E+3


# Log43
# Gap5
# 6-10
# 4 probe femto
# After pumping overnight
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Ch2 Amplifier (x/V): 10.000E-3
# Average resistance: 13.4877E+3

# Log50
# Gap7
# 2-14
# 4 probe femto
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Ch2 Amplifier (x/V): 10.000E-3
# Average resistance: 2.5771E+3


# Log57
# Gap9
# 4-12
# 4 probe femto
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Ch2 Amplifier (x/V): 10.000E-3
# Average resistance: 63.7684E+3
