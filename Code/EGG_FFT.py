# Description: This script reads EGG data from a CSV file and computes the FFT to find the fundamental frequency.

import numpy as np
import pandas as pd
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('yourfilepath.csv')

# Print column names to verify the correct column name
print(df.columns)

# Compute the FFT of the EGG data
# Ensure the column name matches exactly with the one in your CSV file
egg_data = df['EGG']  # Adjust 'EGG' to the correct column name if necessary
egg_fft = fftpack.fft(egg_data)

# Compute the frequencies
n = len(egg_data)
timestep = 1.0 / 1000  # Assuming a sampling rate of 1000 Hz
freq = np.fft.fftfreq(n, d=timestep)


#amplitude = np.abs(egg_fft)
#fundamental_freq = freq[np.argmax(amplitude)]
#print(fundamental_freq)



# Filter frequencies and amplitudes to only consider frequencies above 0.015 Hz
positive_freq_indices = np.where(freq > 0.015)
filtered_freq = freq[positive_freq_indices]
filtered_amplitude = np.abs(egg_fft)[positive_freq_indices]

# Find the fundamental frequency
fundamental_freq = filtered_freq[np.argmax(filtered_amplitude)]
print(fundamental_freq * 60)


# Plot the FFT
plt.figure(figsize=(12, 6))
plt.plot(freq, np.abs(egg_fft))
plt.title('FFT of EGG Data')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim(0, 0.1)  # Limit x-axis to 50 Hz for better visualization
plt.ylim(0,500000000)
plt.grid()
plt.show()