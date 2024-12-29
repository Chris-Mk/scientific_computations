import numpy as np

from masters.high_speed_devices.S_parameter_measurements import converter


def nz2s(nz):
    # nz2s
    # nz2s(nz) converts normalised z-parameters to S-parameters.
    # Optional frequency data in nz[4] is copied into s[4].
    nz = converter.str_complex_converter(nz)


    # copy to get the optional frequency data in nz[4]
    nz2s = np.copy(nz)
    delta1 = ((1 + nz[0]) * (1 + nz[3])) - (nz[1] * nz[2])
    nz2s[0] = ((nz[0] - 1) * (nz[3] + 1) - (nz[2] * nz[1])) / delta1
    nz2s[1] = 2 * nz[2] / delta1
    nz2s[2] = 2 * nz[1] / delta1
    nz2s[3] = ((1 + nz[0]) * (nz[3] - 1) - (nz[2] * nz[1])) / delta1

    return nz2s

