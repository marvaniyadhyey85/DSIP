import numpy as np

import matplotlib.pyplot as plt

signal = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Compute the FFT of the signal

fft_result = np.fft.fft(signal)

# Compute the magnitude and Phase spectrum of the FFT result

magnitude_spectrum = np.abs(fft_result)

Phase_spectrum = np.angle(fft_result)

# Compute the IFFT of the FFT result

reconstructed_signal = np.fft.ifft(fft_result)
plt.figure(figsize=(12, 8))
# Plot the original signal
plt.subplot(3, 1, 1)
plt.plot(signal)
plt.title('Original Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
# Plot the magnitude spectrum
plt.plot(magnitude_spectrum)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency Index')
plt.ylabel('Magnitude')
plt.subplot(3, 1, 3)
# Plot the phase spectrum
plt.plot(Phase_spectrum)
plt.title('Phase Spectrum')
plt.xlabel('Frequency Index')
plt.ylabel('Phase (radians)')
plt.tight_layout()
# Show the plots
plt.show()