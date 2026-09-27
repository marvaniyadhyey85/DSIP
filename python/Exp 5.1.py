import numpy as np
import matplotlib.pyplot as plt

signal = np.array([1,2,3,4,5,6,7,8])

# FFT
fft = np.fft.fft(signal)

# Real and Imaginary
real = np.real(fft)
imag = np.imag(fft)

# Magnitude and Phase
magnitude = np.abs(fft)
phase = np.angle(fft)

# Reconstructed Signal
reconstructed = np.real(np.fft.ifft(fft))

# 4 Plots
plt.figure(figsize=(8,8))

plt.subplot(4,1,1)
plt.stem(real, label="Real")
for i, val in enumerate(real):
    plt.annotate(f'{val:.2f}', (i, val), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
plt.stem(imag, label="Imaginary")
for i, val in enumerate(imag):
    plt.annotate(f'{val:.2f}', (i, val), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=8)
plt.title("FFT Real and Imaginary")
plt.legend()

plt.subplot(4,1,2)
plt.stem(magnitude)
for i, val in enumerate(magnitude):
    plt.annotate(f'{val:.2f}', (i, val), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
plt.title("Magnitude")

plt.subplot(4,1,3)
plt.stem(phase)
for i, val in enumerate(phase):
    plt.annotate(f'{val:.2f}', (i, val), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
plt.title("Phase")

plt.subplot(4,1,4)
plt.stem(reconstructed)
for i, val in enumerate(reconstructed):
    plt.annotate(f'{val:.2f}', (i, val), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
plt.title("Reconstructed Signal")

plt.tight_layout()
plt.show()