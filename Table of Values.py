from sympy import symbols, Eq, solve
from tabulate import tabulate

# Molar Weights (variable name = NameMW). All in g/mol
HMDAmw = 226.27
RM257mw = 588.6
RM257RINGmw = 366.6
EDDETmw = 182.3
PETMPmw = 488.7

# inputs
RingTotalRatio_range = [round(i, 2) for i in list(float(j) / 100 for j in range(0, 51, 3))]
# Range of Ring Total Ratio values from 0.05 to 0.50 with an interval of 0.03
PthalDBDiff = 0.15
SpacerLinkerRatio = 10.36
total_mass = 1.0
SpacerArms = 2
LinkerArms = 3

# Results:
PthalDBRatio = 1 / (1 + PthalDBDiff)

# Define x, y, a, and b as symbols
x, y, a, b = symbols('x y a b')

# Initialize table data list with the header
table_data = [["Ring Total Ratio", "Mass of RM257 (g)", "Mass of HMDA (g)", "Mass of EDDET (g)", "Mass of PETMP (g)", "Total Mass (g)"]]

# Iterate over the Ring Total Ratio range
for RingTotalRatio in RingTotalRatio_range:
    # Equation 1
    eq1 = Eq((x * RM257RINGmw) / total_mass, RingTotalRatio)

    # Equation 2
    eq2 = Eq((2 * PthalDBRatio * (x + y)) / (SpacerArms * SpacerLinkerRatio + LinkerArms) * EDDETmw * SpacerLinkerRatio, a * EDDETmw)

    # Equation 3
    eq3 = Eq(x * RM257mw + y * HMDAmw + a * EDDETmw + b * PETMPmw, total_mass)

    # Equation 4
    eq4 = Eq(b - a / SpacerLinkerRatio, 0)

    # Solving the equations
    solution = solve((eq1, eq2, eq3, eq4), (x, y, a, b))

    # Extracting the values
    x_val = solution[x]
    y_val = solution[y]
    a_val = solution[a]
    b_val = solution[b]

    # Calculate mass of each compound
    mass_RM257 = x_val * RM257mw
    mass_HMDA = y_val * HMDAmw
    mass_EDDET = a_val * EDDETmw
    mass_PETMP = b_val * PETMPmw

    # Add row data to the table_data list
    table_data.append([f"{RingTotalRatio:.2f}", f"{mass_RM257:.5f}", f"{mass_HMDA:.5f}", f"{mass_EDDET:.5f}", f"{mass_PETMP:.5f}", f"{total_mass:.5f}"])

# Create the fancy grid table
table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")

# Print the table
print(table)
