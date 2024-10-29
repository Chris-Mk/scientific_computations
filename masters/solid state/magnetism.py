from matplotlib.pyplot import *
import numpy as np

T = 0.8
B = np.linspace(-1, 1, 100)
m_0 = 0.01
m_1 = 0.01

m_series = np.zeros(len(B))
m_1series = np.zeros(len(B))
chi_series = np.zeros(len(B))
for i in range(len(B) - 1):
    for _ in range(100):
        m_0 = -0.5 * np.tanh((B[i] - 2 * m_0) / T)
        m_1 = (-0.5 * ((B[i] - 2 * m_1) / T)) + ((1 / 6) * ((B[i] - 2 * m_1) / T) ** 3)
    chi = -1 / (2 * T * np.cosh((B[i] - 2 * m_0) / T) ** 2)
    m_series[i] = m_0
    m_1series[i] = m_1
    chi_series[i] = chi

title(f'T={T}')
xlabel('B')
ylabel('m')
plot(B[: 95], m_series[: 95], label='m_series')
plot(B[: 95], m_1series[: 95], label='m_approx')
# plot(B[: 95], chi_series[: 95], label='chi')
legend()
