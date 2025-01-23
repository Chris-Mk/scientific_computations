from matplotlib.pyplot import *
from numpy import *
import scipy.constants as sc

Vds = linspace(0, 1, 100)
Vgs = array([0, 0.1, 0.2, 0.3, 0.4])
epsilon_ox = epsilon_well = 20
t_ox = t_well = 5e-9  # oxide and quantum well thickness
m_eff = 0.2 * sc.m_e  # electron effective mass
gs = gv = 2  # spin and valency degeneracy respectively
T = 300  # temperature in Kelvin

N_c = gs * gv * sqrt(2 * pi * m_eff * sc.k * T * sc.h ** -2)
Cq = (gs * gv * sc.e ** 2 * m_eff) / (2 * pi * sc.hbar ** 2)  # quantum capacitance
Cox = (epsilon_ox * sc.epsilon_0) / t_ox  # gate oxide capacitance
Cc = (epsilon_well * sc.epsilon_0) / (0.36 * t_ox)  # charge centroid capacitance
Cg = ((1 / Cq) + (1 / Cox)) ** -1  # total capacitance in series connection
vth = (sc.k * T) / sc.e  # thermal voltage
nq = (Cq * vth) / sc.e


def current(vds, vgs):
    nu_d = vds / vth
    eta_s = (Cq * vgs) / (sc.e * nq)
    eta_d = eta_s - nu_d
    F_diff = (4 / (3 * sqrt(pi))) * ((eta_s ** 1.5) - (
        0 if eta_d <= 0 else eta_d ** 1.5))  # difference of fermi-dirac integrals of order 1/2
    J = sc.e * sc.h ** -1 * N_c * sc.k * T
    return J * F_diff


for vg in Vgs:
    Ids = array([t_well * current(vd, vg) for vd in Vds])
    plot(Vds, Ids, label='$V_{gs}$=' + str(vg) + 'V')
    legend()

title('$g_v=2, m_c^*=0.2m_e$')
xlabel('$V_{ds}$ [V]')
ylabel('$I_{ds}$ [A]')
ticklabel_format(axis='y', style='sci', scilimits=(0, -5))
# savefig('C:/Users/LENOVO/PycharmProjects/scientific_computations/masters/high_speed_devices/ballisticTransistor.pdf')
show(block=True)
