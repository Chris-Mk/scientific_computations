import sys

from matplotlib.pyplot import *
from numpy import *

A = array([[1, 3, 2], [-3, 4, 3], [2, 3, 1]])
z = array([8, 3, 12])

z_n, v_n, q_n = [z], [z / linalg.norm(z)], []
iterate = 0
for i in range(13):
    z = A @ z
    v = z / linalg.norm(z)
    q = v.T @ A @ v

    z_n.append(z)
    v_n.append(v)
    q_n.append(q)

print("zn =", z_n)
print("vn =", v_n)
print("qn =", q_n)

v_lim = v_n[-1]
q_lim = q_n[-1]
n_iter = 0
for i in range(len(v_n)):
    if linalg.norm(v_n[i] - v_lim) < 1e-8:
        n_iter = i
        break

print("Iterations =", n_iter)


def f(val, arr, lim):
    for k in range(len(arr)):
        if linalg.norm(arr[k] - lim) < val:
            return k


N = 10000
ep = linspace(0.1, 1e-14, N)
v_iter = zeros(N)
q_iter = zeros(N)

for j in range(N):
    v_iter[j] = f(ep[j], v_n, v_lim)
    q_iter[j] = f(ep[j], q_n, q_lim)

plot(ep, v_iter, label="vn")
plot(ep, q_iter, label="qn")
xlabel("epsilon")
ylabel("iterations")
xscale("log")
grid()
legend()
