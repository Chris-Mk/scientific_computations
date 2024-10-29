import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
from masters.spectroscopy import intensityCorrectedWMSFile


# Define intensityCorrectedWMS function (to be replaced by actual implementation)
# def intensityCorrectedWMS(RAM_signal, RAM_info, flag):
#     # Placeholder function. You will need to implement this or import it.
#     # Assuming it returns a dictionary with 'wms' as a key.
#     wms = RAM_signal * np.sin(2 * np.pi * RAM_info['fmod'] * np.arange(len(RAM_signal)) / RAM_info['fsampling'])
#     return {'wms': wms}


# Path
filepath_signal = "./masters/spectroscopy/files/ABS/100avgWms.txt"

# The sampling variables for the lock-in algorithm
RAM_info = {
    'fmod': 9025,  # Modulation frequency in Hz
    'Nsample': 16000,  # Number of points sampled
    'deltafrq': 500,  # Width of bandpass filter
    'fsampling': 400000,  # Sampling frequency in Hz
    'nHarmonic': 20  # Harmonic to calculate
}

# Importing data
data = np.loadtxt(filepath_signal, delimiter='\t', skiprows=26)  # Assuming the .txt file is tab-separated
RAM_signal = data[:RAM_info['Nsample'], 0]  # Extract the signal

# Calculating the WMS signal
wms_temp = intensityCorrectedWMSFile.intensity_corrected_WMS(RAM_signal, RAM_info, 0)
sig_data = np.zeros((1, len(wms_temp['wms'])))
sig_data[0, :] = wms_temp['wms']
raw_data = np.zeros((1, len(RAM_signal)))
raw_data[0, :] = RAM_signal

# FFT and plotting the frequency domain
frq = RAM_info['fsampling'] * np.fft.fftfreq(RAM_info['Nsample'])  # Frequency axis for FFT
fft_amplitude = fftshift(fft(RAM_signal))  # FFT and shift
plt.figure(1)
plt.plot(frq, np.log10(np.abs(fft_amplitude)))
plt.xlabel('Frequency [Hz]')
plt.ylabel('FT Amplitude')
plt.show(block=True)

# Plotting the signal in the time domain
time = np.arange(1, RAM_info['Nsample'] + 1) / RAM_info['fsampling']  # Time axis
plt.figure()
plt.plot(time, sig_data[0, :])
plt.xlabel('Time [s]')
plt.ylabel('WMS Signal')
plt.show(block=True)

plt.figure()
plt.plot(time, raw_data[0, :])
plt.xlabel('Time [s]')
plt.ylabel('Raw Signal')
plt.show(block=True)

# Calculating the mean peak amplitude
meanPeakAmp = (np.max(sig_data[0, :RAM_info['Nsample'] // 2]) + np.max(sig_data[0, RAM_info['Nsample'] // 2:])) * 0.5
print(f"Mean Peak Amplitude: {meanPeakAmp:.6f}")
