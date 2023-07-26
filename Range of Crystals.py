from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
import numpy as np

HMDAmw = 226.27 
RM257mw = 588.6
RM257RINGmw = 366.6
EDDETmw = 182.3
PETMPmw = 488.7

# inputs
RingTotalRatio = 0.47
PthalDBDiff = 0.15
PthalDBRatio = 1/(1 + PthalDBDiff)
SpacerLinkerRatio = 10
EDDETmass = 0.174*2

# Define x and y as symbols
x, y = symbols('x y')

# Define the range of RingTotalRatio values
RingTotalRatio_range = [0.2, 0.3, 0.4, 0.5]

# Lists to store x and y values
x_vals = []
y_vals = []

# Iterate over the RingTotalRatio range
for RingTotalRatio in RingTotalRatio_range:
    # Equation 1
    eq1 = Eq((x * RM257RINGmw) / (x * RM257mw + y * HMDAmw + 0.174 + (0.178 * PETMPmw / EDDETmw) / SpacerLinkerRatio),
             RingTotalRatio)

    # Equation 2
    eq2 = Eq((2 * DBPthalRatio * (x + y)) / (2 * SpacerLinkerRatio + 3) * 182.3 * SpacerLinkerRatio, 0.174)

    # Solving the equations
    solution = solve((eq1, eq2), (x, y))

    # Extracting the values
    x_val = round(float(solution[x]), 5)
    y_val = round(float(solution[y]), 5)

    x_vals.append(x_val)
    y_vals.append(y_val)

    # Creating a chart
    plt.plot(x_val, y_val, 'o', label=f'RingTotalRatio = {RingTotalRatio}')

# Computing line of best fit
coefficients = np.polyfit(x_vals, y_vals, 1)
poly_eq = np.poly1d(coefficients)
x_range = np.linspace(np.min(x_vals), np.max(x_vals), 100)
y_range = poly_eq(x_range)

# Plotting line of best fit
plt.plot(x_range, y_range, 'r-', label=f'Line of Best Fit: y = {round(poly_eq.coefficients[0], 5)}x + {round(poly_eq.coefficients[1], 5)}')

# Adding labels and legend to the chart
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Displaying the chart
plt.show()
