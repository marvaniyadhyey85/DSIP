import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Step 1: Filter parameters
N = 31

# Step 2: Design four FIR filters
low = firwin(N, 3000, window='hann',
             pass_zero='lowpass', fs=10000)

high = firwin(N, 3000, window='hann',
              pass_zero='highpass', fs=10000)

band = firwin(N, [1000, 6000], window='hann',
              pass_zero='bandpass', fs=13000)

reject = firwin(N, [1000, 6000], window='hann',
                pass_zero='bandstop', fs=13000)

# Step 3: Calculate frequency responses
filters = [low, high, band, reject]
titles = ['Low-Pass Filter', 'High-Pass Filter',
          'Band-Pass Filter', 'Band-Reject Filter']

# Step 4: Plot all graphs
plt.figure(figsize=(10, 8))

for i in range(4):
    f, H = freqz(filters[i], worN=2048, fs=10000)
    magnitude_db = 20 * np.log10(np.maximum(np.abs(H), 1e-10))

    plt.subplot(2, 2, i + 1)
    plt.plot(f, magnitude_db)
    plt.title(titles[i])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid()

plt.tight_layout()
plt.show()
# impluse response
n = np.arange(N)

plt.figure(figsize=(10, 8))

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.stem(n, filters[i])
    plt.title(titles[i])
    plt.xlabel('Sample (n)')
    plt.ylabel('Amplitude')
    plt.grid()

plt.tight_layout()
plt.show()
# Phase Response
Fs = 10000  # Sampling frequency
plt.figure(figsize=(10, 8))

for i in range(4):
    f, H = freqz(filters[i], worN=2048, fs=Fs)

    phase = np.unwrap(np.angle(H))

    plt.subplot(2, 2, i + 1)
    plt.plot(f, phase)
    plt.title(titles[i])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (Radians)')
    plt.grid()

plt.tight_layout()
plt.show()