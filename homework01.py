import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# task 01
# =============================================================================

approx_array = []


def approx_ln(x, n):
    a_initial = (1 + x) / 2
    g_initial = np.sqrt(x)

    for i in range(n):
        approx = (x - 1) / a_initial
        approx_array.append(approx)

        a_next = (a_initial + g_initial) / 2
        g_next = np.sqrt(a_next * g_initial)

        if np.abs(approx - np.log(x)) < 1e-8:
            return f"Success! \nln({x}) = {np.log(x)}\napprox = {approx}"

        a_initial = a_next
        g_initial = g_next
    return f"Failed! \nln({x})= {np.log(x)}\napprox={(x-1)/a_initial}"


print(approx_ln(2, 100))

# =============================================================================
# task 02
# =============================================================================

ln = [np.log(i) for i in range(1, len(approx_array))]
plt.plot(ln, label="ln(x)")
plt.plot(approx_array, label="approx_ln")
plt.legend()
plt.show()

error = [np.abs(approx_array[i] - ln[i]) for i in range(len(ln))]
plt.plot(error)
plt.show()

# =============================================================================
# task 03
# =============================================================================


