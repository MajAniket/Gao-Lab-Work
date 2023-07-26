from sympy import symbols, Eq, solve
from tabulate import tabulate
import questionary

# Prompt the user for input values with default values
PthalDBDiff = questionary.text("Enter the PthalDB difference: (Default = 0.15)", default="0.15").ask()
SpacerLinkerRatio = questionary.text("Enter the Spacer Linker Ratio: (Default = 10.36)", default="10.36").ask()
total_mass = questionary.text("Enter the total mass (g): (Default = 1)", default="1").ask()
SpacerArms = questionary.text("Enter the number of spacer arms: (Default = 2)", default="2").ask()
LinkerArms = questionary.text("Enter the number of linker arms: (Default = 3)", default="3").ask()

# Convert the input values to appropriate data types
PthalDBDiff = float(PthalDBDiff)
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
Tolmw = 92.13842

# Results:
# Results:
PthalDBRatio = 1 / (1 + PthalDBDiff)

# Define x, y, a, and b as symbols
x, y, a, b = symbols('x y a b')

# Initialize table data list with the header
table_data = [["Ring Total Ratio", "Moles of RM257", "Moles of Toluene", "Moles of HMDA", "Moles of EDDET", "Moles of PETMP", "Total Mass of Elastomer", "Total Mass"]]

# Constant moles for PETMP
moles_PETMP_constant = 0.047 / PETMPmw

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

    # Calculate moles of each compound
    moles_RM257 = x_val
    moles_HMDA = y_val

    # Calculate moles of Toluene
    moles_Toluene = moles_RM257 * 0.31 / 0.77

    # Calculate moles of PETMP at the current Ring Total Ratio
    moles_PETMP = moles_PETMP_constant

    # Calculate moles of EDDET at the current Ring Total Ratio
    moles_EDDET = SpacerLinkerRatio * moles_PETMP * PETMPmw / EDDETmw

    # Calculate total mass of the elastomer
    elastomer_mass = moles_RM257 * RM257mw + moles_HMDA * HMDAmw + moles_EDDET * EDDETmw + moles_PETMP * PETMPmw

    # Add row data to the table_data list
    table_data.append([f"{RingTotalRatio:.2f}", f"{moles_RM257:.5f}", f"{moles_Toluene:.5f}", f"{moles_HMDA:.5f}", f"{moles_EDDET:.5f}", f"{moles_PETMP:.5f}", f"{elastomer_mass:.5f}", f"{total_mass:.5f}"])

# Create the fancy grid table
table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")

# Print the table
print(table)
