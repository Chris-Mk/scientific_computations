from matplotlib.pyplot import *
import pandas as pd
from scipy.stats import linregress

data1 = pd.read_csv("./thesis/electrical_measurements/CM02-57/cm02 LOG_5.txt", "\t", header=1,
                    names=["Time(s):", "Sweep V(V):", "Ch1 I1(A):", "Ch1 I2(A):"])
data = pd.read_csv("./thesis/data/electrical_measurements/data LOG_25.txt", "\t", header=1,
                   names=["Time(s):", "Sweep V(V):", "Ch1 I1(A):", "Ch1 I2(A):"])

I1 = (data1["Ch1 I1(A):"] + data1["Ch1 I2(A):"]) / 200
V1 = data1["Sweep V(V):"] / 10
m1, y_inter1, *a1 = linregress(V1, I1)

I = (data["Ch1 I1(A):"] + data["Ch1 I2(A):"]) / 200
V = data["Sweep V(V):"] / 10
m, y_inter, *a = linregress(V, I)

# subplot(121)
grid()
# xlabel("I [A]")
# ylabel("V [V]")
ylabel("I [A]")
xlabel("V [V]")
title("Two-probe measurement")
ticklabel_format(axis="both", style="sci", scilimits=(0, 0))
# ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
# text(-4.5e-9, 0.8e-3, f"Initial Resistance={((m1 * 10) - 100):.0f}$\Omega$", fontsize=12)
# text(-4.5e-9, 0.8e-3, f"Initial Resistance={((m1 * 10) - 100):.0f}$\Omega$", fontsize=12)
text(-1e-3, 6e-9, f"Initial Resistance={((1 / m1) / 10 - 100):.0f}$\Omega$", fontsize=12)
text(-1e-3, 5e-9, f"Final Resistance={((1 / m ) / 10 - 100):.0f}$\Omega$", fontsize=12)

plot(V1, I1, "go")
plot(V1, m1 * V1 + y_inter1, label="Without Milling")
plot(V, I, "go")
plot(V, m * V + y_inter, label="With Milling")

# plot(I1, V1, "ro")
# plot(I1, m1 * I1 + y_inter1, label="Without Milling")
# plot(I, V, "go")
# plot(I, m * I + y_inter, label="With Milling")
legend(loc="lower right")

# data = pd.read_csv("./thesis/data/electrical_measurements/data LOG_23.txt", "\t", header=1,
#                    names=["Time(s):", "Sweep V(V):", "Ch1 I1(A):", "Ch1 I2(A):", "Ch2 V1(V):", "Ch2 V2(V):"])
#
# I = (data["Ch1 I1(A):"] + data["Ch1 I2(A):"]) / 200
# V = (data["Ch2 V1(V):"] + data["Ch2 V2(V):"]) / 2
# m, y_inter, *a = linregress(I, V)
#
# subplot(122)
# grid()
# xlabel("I [nA]")
# ylabel("V [mV]")
# title("Four-probe measurement")
# ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
# text(-1.1e-8, 2.5e-3, f"Resistance={(m / 100) - 100:.2f}$\Omega$", fontsize=12)
# plot(I, V, "ro")
# plot(I, m * I + y_inter)

# Log7 - preferred data over Log29
# Gap1
# 14-2

# Log25
# Gap3
# 4-12
# After pumping overnight
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Average resistance: 1.6949E+3


# Log29
# Gap1
# 2-14
# After pumping overnight
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Average resistance: 2.3760E+3


# Log40
# Gap5
# 6-10
# After pumping overnight
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Average resistance: 1.9967E+3


# Log48
# Gap7
# 2-14
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Average resistance: 4.6615E+3


# Log55
# Gap9
# 12-4
#
# SOURCE A1: V (DC) SR830#1 Aux 3
#  (Start:Stop:Step:Div) : (-0.1 : 0.1 : 0.01 : 100)
# Ch1 Amplifier (x/V): 200.000E-9
# Average resistance: 97.8505E+3
