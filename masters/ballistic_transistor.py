from matplotlib.pyplot import *
from numpy import *
import scipy.constants as sc

Vds = linspace(0.1, 1, 100)
Vgs = array([0.1, 0.2, 0.3, 0.4])
epsilon_ox = epsilon_well = 20
t_ox = t_well = 5e-9  # oxide and quantum well thickness
m_eff = 0.2 * sc.m_e  # electron effective mass
gs = gv = 2  # spin and valency degeneracy respectively
T = 300  # temperature in Kelvin

N_c = gs * gv * sqrt(2 * pi * m_eff * sc.k * T * sc.h ** -2)
Cq = (gs * gv * sc.e ** 2 * m_eff) / (2 * pi * sc.hbar ** 2)  # quantum capacitance
Cox = (epsilon_ox * sc.epsilon_0) / t_ox  # gate oxide capacitance
Cc = (epsilon_well * sc.epsilon_0) / (0.36 * t_ox)  # charge centroid capacitance
Cg = ((1 / Cq) + (1 / Cc) + (1 / Cox)) ** -1  # total capacitance in series connection


def current(vds, vgs):
    ns = Cg * vgs  # charge concentration above subthreshold regime
    E_diff = (sc.e ** 2 * ns) / Cq  # E_fs - Ec (energy difference between the fermi-level and conduction band edge
    eta_s = E_diff / (sc.k * T)
    eta_d = eta_s - ((sc.e * vds) / (sc.k * T))
    F = (4 / (3 * sqrt(pi))) * (eta_s ** 1.5 - eta_d ** 1.5)  # difference of fermi-dirac integrals of order 1/2
    return sc.e ** 2 * sc.h ** -1 * N_c * sc.k * T * sc.e ** -1 * F


for vg in Vgs:
    Ids = array([current(vd, vg) for vd in Vds])
    plot(Vds, Ids, label='Vgs=' + str(vg))
    legend()
xlabel('$V_{ds}$')
ylabel('$I_{ds}$')
show(block=True)
