import numpy as np
# from scipy import polyfit, polyval
from masters.spectroscopy import Lockin_AmplifierFile


def intensity_corrected_WMS(RAM_signal, RAM_info, bg):
    # Set the configuration
    config1_down1 = 20
    config1_up1 = 21
    donfig2_down1 = np.floor(16 * 20 / 80).astype(int)
    donfig2_up1 = donfig2_down1 + 1
    config1_down2 = 899
    config1_up2 = 900
    config2_down2 = np.floor(16 * 899 / 80).astype(int)
    config2_up2 = config2_down2 + 1
    nHarmonic = RAM_info['nHarmonic']

    # Calculate the nf signal
    correct_WMS = Lockin_AmplifierFile.Lockin_Amplifier(RAM_signal, RAM_info, nHarmonic)

    # Calculate the intensity of the ramp, up segment
    upX1 = np.arange(np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * donfig2_down1),
                     np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * donfig2_up1), dtype=int)
    upX2 = np.arange(np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * config2_down2),
                     np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * config2_up2), dtype=int)

    upseg1 = RAM_signal[upX1]
    upseg2 = RAM_signal[upX2]

    p = np.polyfit([np.ceil(np.mean(upX1)), np.ceil(np.mean(upX2))],
                [np.mean(upseg1), np.mean(upseg2)], 1)

    X1 = np.linspace(0, np.ceil(RAM_info['Nsample'] / 2) - 1, int(np.ceil(RAM_info['Nsample'] / 2)))
    y1 = np.polyval(p, X1)

    # Calculate the intensity of the ramp, down segment
    downX1 = np.arange(np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * donfig2_down1 + RAM_info['Nsample'] / 2),
                       np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * donfig2_up1 + RAM_info['Nsample'] / 2),
                       dtype=int)
    downX2 = np.arange(np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * config2_down2 + RAM_info['Nsample'] / 2),
                       np.ceil(RAM_info['fsampling'] / RAM_info['fmod'] * config2_up2 + RAM_info['Nsample'] / 2),
                       dtype=int)

    downseg1 = RAM_signal[downX1]
    downseg2 = RAM_signal[downX2]

    p = np.polyfit([np.ceil(np.mean(downX1)), np.ceil(np.mean(downX2))],
                [np.mean(downseg1), np.mean(downseg2)], 1)

    X2 = np.linspace(np.ceil(RAM_info['Nsample'] / 2), RAM_info['Nsample'] - 1, int(np.ceil(RAM_info['Nsample'] / 2)))
    y2 = np.polyval(p, X2)

    # Intensity calibrate the WMS signal
    correct_WMS['wms'] = correct_WMS['wms'] / (np.concatenate((y1, y2)) - bg)

    return correct_WMS
