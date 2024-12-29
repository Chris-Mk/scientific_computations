import numpy as np


def str_complex_converter(x):
    data = np.zeros(x.shape, dtype=complex)
    for i in range(len(x)):
        data[i] = complex(x[i])
    return data
