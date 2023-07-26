from sympy import symbols, Eq, solve

# Molar Weights (variable name = NameMW). All in g/mol
HMDAmw = 226.27 
RM257mw = 588.6
RM257RINGmw = 366.6
EDDETmw = 182.3
PETMPmw = 488.7

# inputs
RingTotalRatio = 0.1
# mass of rings/mass of total elastomer
PthalDBDiff = 0.15
# There are x% more Double Bonds than Pthalates
SpacerLinkerRatio = 10.36
# mole ratio of Spacer:Linker (EDDET:PETMP)
total_mass = 1.0
# total mass of elastomer
SpacerArms = 2
# number of Arms in spacer
LinkerArms = 3
# Number of Arms in the Linker
# Results:
PthalDBRatio = 1 / (1 + PthalDBDiff)

# Define x, y, a, and b as symbols
x, y, a, b = symbols('x y a b')

# Equation 1
eq1 = Eq((x * RM257RINGmw) / total_mass, RingTotalRatio)

# Equation 2
eq2 = Eq((2 * PthalDBRatio * (x + y)) / (SpacerArms * SpacerLinkerRatio + LinkerArms) * EDDETmw * SpacerLinkerRatio, a*EDDETmw)

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

print("Solution:")
print("mass of RM257:", x_val * RM257mw, "grams")
print("mass of HMDA:", y_val * HMDAmw, "grams")
print("mass of EDDET:", a_val*EDDETmw, "grams")
print("mass of PETMP:", b_val*PETMPmw, "grams")
print("total mass:", (x_val * RM257mw + y_val * HMDAmw + a_val * EDDETmw + b_val * PETMPmw), "grams")