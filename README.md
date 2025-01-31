# Fourier Series Analysis of a Square Wave

This project analyzes a square wave using Fourier series expansion and Discrete Fourier Transform (DFT). It was developed as part of a **Mathematical Engineering project in Winter 2025 at KNTU**, using **Python** along with **pandas** and **matplotlib** libraries.

## Overview
- **Generates a square wave** with a specified frequency and amplitude.
- **Computes and visualizes its Fourier Transform (DFT)** using `numpy.fft`.
- **Calculates the Fourier Series coefficients** for harmonic analysis.
- **Reconstructs the square wave** using a limited number of harmonics.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy matplotlib pandas
```

## Implementation Details
1. **Square Wave Generation**  
   - A time-domain signal is created using `numpy.sign(np.sin(...))`.
   - Plotted using `matplotlib`.

2. **Fourier Transform (DFT) Analysis**  
   - The **Discrete Fourier Transform (DFT)** of the signal is computed using `numpy.fft.fft`.
   - The corresponding frequencies are obtained using `numpy.fft.fftfreq`.

3. **Fourier Series Coefficients Calculation**  
   - The Fourier series expansion of the square wave consists of **only odd harmonics**.
   - The coefficients are computed as:  
     \[
     b_n = \frac{4A}{n\pi}, \quad n = 1,3,5,7,\dots
     \]
   - Plotted using `matplotlib.stem`.

4. **Reconstruction of Square Wave**  
   - The signal is reconstructed using a **finite number of harmonics**.
   - Summation of sine functions with the calculated coefficients.

## Results
- **The original square wave** and **its reconstructed version** (using a limited number of harmonics) are compared.
- **The frequency spectrum (DFT)** illustrates the primary harmonic components.
- **The Fourier coefficients** graph shows the decreasing trend of harmonics.

## How to Run
Run the Python script:
```bash
python fourier_square_wave.py
```

This will generate all the visualizations step by step.

## Applications
- **Signal Processing**
- **Fourier Analysis**
- **Mathematical Modeling**
- **Audio and Speech Processing**
```
