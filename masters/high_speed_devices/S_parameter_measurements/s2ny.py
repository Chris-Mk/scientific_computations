import numpy as np

from masters.high_speed_devices.S_parameter_measurements import converter


def s2ny(s):
    # s2ny
    # s2ny(s) converts S-parameters to normalized y-parameters.
    # Optional frequency data in s[4] is copied into ny[4].
    s = converter.str_complex_converter(s)

    delta6 = ((1 + s[0]) * (1 + s[3])) - (s[2] * s[1])
    # copy to get the optional frequency data in s[4].
    s2ny = np.copy(s)
    s2ny[0] = ((1 - s[0]) * (1 + s[3]) + (s[2] * s[1])) / delta6
    s2ny[1] = -2 * s[2] / delta6
    s2ny[2] = -2 * s[1] / delta6
    s2ny[3] = ((1 + s[0]) * (1 - s[3]) + (s[2] * s[1])) / delta6

    return s2ny
