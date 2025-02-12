import numpy as np
import matplotlib.pyplot as plt

frequency = 100
amplitude = 1
duration = 0.02
sampling_rate = 10000

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

square_wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))

plt.figure(figsize=(10, 4))
plt.plot(t, square_wave)
plt.title('Square Wave Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

fft_result = np.fft.fft(square_wave)
frequencies = np.fft.fftfreq(len(square_wave), 1/sampling_rate)

plt.figure(figsize=(10, 4))
plt.plot(frequencies, np.abs(fft_result))
plt.title('Frequency Spectrum (DFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim(0, 500)
plt.grid(True)
plt.show()

num_harmonics = 20
fourier_coeffs = []
for n in range(1, num_harmonics + 1):
    if n % 2 != 0:
        bn = (4 * amplitude) / (n * np.pi)
        fourier_coeffs.append(bn)
    else:
        fourier_coeffs.append(0)

plt.figure(figsize=(10, 4))
n_values = np.arange(1, num_harmonics + 1)
plt.stem(n_values, fourier_coeffs)
plt.title('Fourier Series Coefficients')
plt.xlabel('n (Harmonic Number)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

reconstructed_signal = np.zeros_like(t)
for n in range(1, num_harmonics + 1, 2):
    reconstructed_signal += (4 * amplitude / (n * np.pi)) * np.sin(2 * np.pi * n * frequency * t)

plt.figure(figsize=(10, 4))
plt.plot(t, square_wave, label='Original Signal')
plt.plot(t, reconstructed_signal, label='Reconstructed Signal')
plt.title('Signal Reconstruction using Fourier Series')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
