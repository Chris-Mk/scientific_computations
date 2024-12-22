import numpy as np


def Lockin_Amplifier(RAM_signal, RAM_info, nHarmonic):
    # Frequency array
    frq = RAM_info['fsampling'] * np.arange(-np.ceil(RAM_info['Nsample'] / 2),
                                            np.ceil(RAM_info['Nsample'] / 2)) / RAM_info['Nsample']

    nshift = RAM_info['fmod'] / (RAM_info['fsampling'] / RAM_info['Nsample'])

    # Filter out the harmonic signal
    bandpass_signal = (np.fft.fftshift(np.fft.fft(RAM_signal)) *
                       np.exp(-1.0 * ((frq - nHarmonic * RAM_info['fmod']) / RAM_info['deltafrq']) ** 8))

    # Construct harmonic signal in time domain via inverse FFT
    WMS_data = {}
    WMS_data['wms'] = np.fft.ifft(np.fft.fftshift(np.roll(bandpass_signal, -int(nHarmonic * nshift))))

    # Mean value
    WMS_data['meanValue'] = np.mean(WMS_data['wms'])

    # Mean phase shift (alpha)
    WMS_data['alpha'] = np.angle(WMS_data['meanValue'])

    # Estimate phase shift (beta)
    max_idx = np.argmax(np.abs(WMS_data['wms'] - WMS_data['meanValue']))
    WMS_data['wms'] = WMS_data['wms'] - WMS_data['meanValue']
    WMS_data['beta'] = np.angle(WMS_data['wms'][max_idx])

    # Original signal
    WMS_data['wms'] = 2 * np.real(WMS_data['wms'] * np.exp(-1j * WMS_data['beta']))
    WMS_data['meanValue'] = np.abs(WMS_data['meanValue'] * 2)

    return WMS_data
