import matplotlib.pyplot as plt
import numpy as np

# Set the font to "Helvetica Neue" and font size to 24
plt.rcParams["font.family"] = "Helvetica Neue"
plt.rcParams["font.size"] = 24

# Input data
percentage = np.array([20, 30, 40, 48])
youngs_modulus = np.array([0.238, 0.27, 0.408, 0.517])
break_point = np.array([0.105, 0.446, 1.29, 3.27])

# Add error bars to Young's Modulus and Break Point data
youngs_modulus_error = np.array([0.03, 0.035, 0.025, 0.04])
break_point_error = np.array([0.015, 0.01, 0.035, 0.02])

# Updated equations for exponential fit
youngs_modulus_line = 0.123 * np.exp(0.0297 * percentage)
break_point_line = 0.0128 * np.exp(0.116 * percentage)

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 8))  # Make the figure wider

# Plot Young's Modulus on the first y-axis (left) with error bars
ax1.errorbar(percentage, youngs_modulus, yerr=youngs_modulus_error, fmt='o', color='blue', label="Young's Modulus")
ax1.plot(percentage, youngs_modulus_line, '-', color='blue', label="Young's Modulus Fit")
ax1.set_xlabel('Crystal Percentage')
ax1.set_ylabel("Young's Modulus", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis on the right side for the Break Point with error bars
ax2 = ax1.twinx()
ax2.errorbar(percentage, break_point, yerr=break_point_error, fmt='o', color='red', label="Break Point")
ax2.plot(percentage, break_point_line, '-', color='red', label="Break Point Fit")
ax2.set_ylabel('Break Point', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Combine both equations into a single text
table_text = """
Young's Modulus: $E = 0.123 \cdot e^{0.0297 \cdot x}$
Break Point: $B = 0.0128 \cdot e^{0.116 \cdot x}$
"""

# Display the table of equations at the top of the graph
plt.figtext(0.5, 0.905, table_text, fontsize=24, ha='center', va='top', bbox=dict(boxstyle='round,pad=0.1', facecolor='white', alpha=0))

plt.grid(True)
plt.title("Young's Modulus and Break Point as a Function of Crystal Percentage", fontsize=24, fontname='Helvetica Neue')
plt.tight_layout(pad=1.5, h_pad=2)  # Adjust padding around the plot area
plt.show()
