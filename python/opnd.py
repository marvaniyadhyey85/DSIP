import numpy as np
import matplotlib.pyplot as plt
import librosa
import soundfile as sf
from scipy.signal import convolve



audio_file = r"E:\vs code\vscode\python\iphone.mpeg.mpeg"

# Load MPEG audio
audio, sample_rate = librosa.load(audio_file, sr=None, mono=True)

print("Sample Rate =", sample_rate)
print("Total Samples =", len(audio))



ir1 = np.array([1.0])
ir2 = np.array([1.0, 0.5])
ir3 = np.array([1.0, -1.0])

impulse_responses = [ir1, ir2, ir3]



plt.figure(figsize=(10,4))
plt.plot(audio)
plt.title("Original Audio")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()


for i, kernel in enumerate(impulse_responses):

    print(f"\nProcessing IR {i+1}")

    # Convolution
    convoluted = convolve(audio, kernel, mode="same")

    # Normalize
    max_val = np.max(np.abs(convoluted))
    if max_val != 0:
        convoluted = convoluted / max_val

    # Save convoluted audio
    sf.write(f"IR{i+1}_Convolution.wav", convoluted, sample_rate)

    # Inverse filter
    inverse_kernel = kernel[::-1]

    restored = convolve(convoluted, inverse_kernel, mode="same")

    # Normalize
    max_val = np.max(np.abs(restored))
    if max_val != 0:
        restored = restored / max_val

    # Save restored audio
    sf.write(f"IR{i+1}_Inverse.wav", restored, sample_rate)

  

    plt.figure(figsize=(10,8))

    plt.subplot(3,1,1)
    plt.plot(audio)
    plt.title("Original Audio")
    plt.grid(True)

    plt.subplot(3,1,2)
    plt.plot(convoluted)
    plt.title(f"Convolution Output - IR {i+1}")
    plt.grid(True)

    plt.subplot(3,1,3)
    plt.plot(restored)
    plt.title(f"Inverse Filter Output - IR {i+1}")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

print("\nProgram Completed Successfully.")