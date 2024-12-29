import numpy as np
import masters.high_speed_devices.S_parameter_measurements.converter as converter


def s2nz(s):
    # s is an array of complex numbers in str
    # s2nz
    # s2nz(s) converts S-parameters to normalized z-parameters.
    # Optional frequency data in s[4] is copied into nz[4].
    s = converter.str_complex_converter(s)

    delta5 = ((1 - s[0]) * (1 - s[3])) - (s[2] * s[1])
    # copy to get the optional frequency data in s[4].
    s2nz = np.copy(s)
    s2nz[0] = (((1 + s[0]) * (1 - s[3])) + (s[2] * s[1])) / delta5
    s2nz[1] = 2 * s[2] / delta5
    s2nz[2] = 2 * s[1] / delta5
    s2nz[3] = ((1 - s[0]) * (1 + s[3] + (s[2] * s[1]))) / delta5

    return s2nz
