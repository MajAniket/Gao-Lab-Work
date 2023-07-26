from sympy import symbols, Eq, solve
from tabulate import tabulate
import questionary
import math
import csv


# Prompt the user for input values with default values
ThiolDBDiff = questionary.text("Enter the ThiolDB difference: (Default = 0.15)", default="0.15").ask()
SpacerLinkerRatio = questionary.text("Enter the Spacer Linker Ratio: (Default = 10.36)", default="10.36").ask()
total_mass = questionary.text("Enter the total mass (g): (Default = 1)", default="1").ask()
SpacerArms = questionary.text("Enter the number of spacer arms: (Default = 2)", default="2").ask()
LinkerArms = questionary.text("Enter the number of linker arms: (Default = 3)", default="3").ask()

# Convert the input values to appropriate data types
ThiolDBDiff = float(ThiolDBDiff)
SpacerLinkerRatio = float(SpacerLinkerRatio)
total_mass = float(total_mass)
SpacerArms = int(SpacerArms)
LinkerArms = int(LinkerArms)

# Prompt the user for the lower bound, upper bound, and interval of RingTotalRatio_range with default values
lower_bound = questionary.text("Enter the lower bound of Ring Total Ratio: (Default = 0)", default="0").ask()
upper_bound = questionary.text("Enter the upper bound of Ring Total Ratio: (Default = 0.48, more than lower bound)", default="0.48").ask()
interval = questionary.text("Enter the interval length for Ring Total Ratio: (Default = 0.02)", default="0.02").ask()

# Convert the bounds and interval to appropriate data types
lower_bound = float(lower_bound)
upper_bound = float(upper_bound)
interval = float(interval)

# Generate the RingTotalRatio_range based on the user input
RingTotalRatio_range = [round(i, 2) for i in list(j / 100 for j in range(int(lower_bound * 100), int((upper_bound + interval) * 100), int(interval * 100)))]

# Molar Weights (variable name = NameMW). All in g/mol
HMDAmw = 226.27
RM257mw = 588.6
RM257RINGmw = 366.6
EDDETmw = 182.3
PETMPmw = 488.7
Tolmw = 92.14

# Results:
ThiolDBRatio = 1 / (1 + ThiolDBDiff)

# Define x, y, a, and b as symbols
x, y, a, b = symbols('x y a b')

# Initialize table data list with the updated header
table_data = [["Ring Total Ratio", "Mass of RM257 (g)", "Mass of Toluene (g)", "Mass of HMDA (g)", "Mass of EDDET (g)", "Mass of PETMP (g)", "Total Mass (g)", "Young's Modulus", "Break Point"]]

# Iterate over the Ring Total Ratio range
for RingTotalRatio in RingTotalRatio_range:
    # Equation 1
    eq1 = Eq((x * RM257RINGmw) / total_mass, RingTotalRatio)

    # Equation 2
    eq2 = Eq((2 * ThiolDBRatio * (x + y)) / (SpacerArms * SpacerLinkerRatio + LinkerArms) * EDDETmw * SpacerLinkerRatio, a * EDDETmw)

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

    # Calculate mass of Toluene
    mass_Toluene = mass_RM257 * 0.31 / 0.77

    # Calculate Young's Modulus and Break Point
    if RingTotalRatio >= 0.15:
        youngs_modulus = round(0.123 * math.exp(0.0297 * (RingTotalRatio * 100)), 4)
        break_point = round(0.0128 * math.exp(0.116 * (RingTotalRatio * 100)), 4)
    else:
        youngs_modulus = "---"
        break_point = "---"

    # Add row data to the table_data list
    table_data.append([f"{RingTotalRatio:.2f}", f"{mass_RM257:.5f}", f"{mass_Toluene:.5f}", f"{mass_HMDA:.5f}", f"{mass_EDDET:.5f}", f"{mass_PETMP:.5f}", f"{total_mass:.5f}", f"{youngs_modulus}", f"{break_point}"])

# Create the fancy grid table
table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")

# Print the table
print(table)


