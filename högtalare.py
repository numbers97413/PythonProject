import numpy as np
import matplotlib.pyplot as plt

# Filter data for Left Speaker
left_frequencies = [41.8, 121, 139, 205, 305, 567, 1707, 3373]
left_gains = [-7.3, -3.0, 1.4, -5.6, -4.5, -3.4, -2.6, -3.2]
left_q_values = [5.278, 16.931, 3.735, 3.478, 3.691, 3.326, 4.992, 3.738]

# Filter data for Right Speaker
right_frequencies = [40.85, 145, 153.5, 166, 254, 325, 443, 651, 785, 1681, 1915, 2867, 9549]
right_gains = [-10.3, 2.9, -2.2, -5.8, -3.7, 3.2, -4.2, 3.0, -1.8, -5.9, 5.3, -5.1, -2.8]
right_q_values = [4.711, 4.424, 9.747, 5.837, 2.917, 7.492, 1.011, 7.449, 4.845, 4.795, 1.404, 1.001, 1.023]

# Frequency range for plotting (logarithmic scale from 20 Hz to 20 kHz)
freq_range = np.logspace(np.log10(20), np.log10(20000), 1000)

# Function to calculate the frequency response of a parametric EQ filter
def parametric_eq_response(freq, fc, gain, q):
    w = 2 * np.pi * freq
    wc = 2 * np.pi * fc
    alpha = np.sin(wc / (2 * q)) / (wc / (2 * q))  # Simplified alpha for bandwidth
    A = 10**(gain / 40)  # Convert gain from dB to linear
    # Parametric EQ formula (simplified)
    h = 1 + alpha * A * (w / wc - wc / w) + alpha**2 * (1 - 4 * (w / wc)**2)
    # Compute magnitude in dB, avoiding log(0) issues
    h_mag = np.abs(h)
    h_mag = np.where(h_mag > 0, h_mag, 1e-10)  # Avoid log(0) by setting small values
    return 20 * np.log10(h_mag)

# Initialize response arrays
left_response = np.zeros_like(freq_range, dtype=float)
right_response = np.zeros_like(freq_range, dtype=float)

# Calculate the cumulative response for Left Speaker
for fc, gain, q in zip(left_frequencies, left_gains, left_q_values):
    filter_response = parametric_eq_response(freq_range, fc, gain, q)
    left_response += filter_response

# Calculate the cumulative response for Right Speaker
for fc, gain, q in zip(right_frequencies, right_gains, right_q_values):
    filter_response = parametric_eq_response(freq_range, fc, gain, q)
    right_response += filter_response

# Plotting
plt.figure(figsize=(12, 6))
plt.semilogx(freq_range, left_response, label='Left Speaker', color='blue')
plt.semilogx(freq_range, right_response, label='Right Speaker', color='orange')
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)  # Reference flat response
plt.title('Frequency Response Adjustment for Left and Right Speakers')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.xlim(20, 20000)
plt.ylim(-15, 10)  # Adjusted to show the range of gains (e.g., -10.3 to +5.3 dB)
plt.show()