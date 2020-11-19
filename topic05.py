import numpy as np

# =============================================================================
# continued fraction 1 + 1/(1 + 1/...)
# =============================================================================
a_initial = 1

while True:
    a_next = 1 / (1 + a_initial)

    if abs(a_next - a_initial) < 1e-16:
        print(a_initial)
        break

    a_initial = a_next

# =============================================================================
# continued square root sqrt(1 + sqrt(1 + ...)
# =============================================================================

b_initial = 1

while True:
    b_next = np.sqrt(1 + b_initial)

    if abs(b_next - b_initial) < 1e-8:
        print(b_initial)
        break

    b_initial = b_next
