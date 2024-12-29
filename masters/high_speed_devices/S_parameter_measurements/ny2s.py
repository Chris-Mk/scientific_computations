import numpy as np

from masters.high_speed_devices.S_parameter_measurements import converter


def ny2s(ny):
    # ny2s
    # ny2s(ny) converts normalised y-parameters to S-parameters.
    # Optional frequency data in ny[4] is copied into s[4].
    ny = converter.str_complex_converter(ny)

    # copy to get the optional frequency data in ny[4]
    ny2s = np.copy(ny)
    delta2 = (1 + ny[0]) * (1 + ny[3]) - ny[1] * ny[2]
    ny2s[0] = ((1 - ny[0]) * (1 + ny[3]) + ny[2] * ny[1]) / delta2
    ny2s[1] = -2 * ny[1] / delta2
    ny2s[2] = -2 * ny[2] / delta2
    ny2s[3] = ((1 + ny[0]) * (1 - ny[3]) + ny[2] * ny[1]) / delta2

    return ny2s
