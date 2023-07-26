import py3Dmol
HMDAmw = 226.27
RM257mw = 588.6
RM257RINGmw = 366.6
EDDETmw = 182.3
PETMPmw = 488.7
Tolmw = 92.14


# Create a Py3Dmol view
view = py3Dmol.view(width=400, height=400)

# Read the mol file
with open('MolView.mol', 'r') as file:
    mol_data = file.read()

# Load the molecule data into the view
view.addModel(mol_data, 'mol')

# Set the style and display options
view.setStyle({'stick': {}})
view.zoomTo()

# Show the view
view.show()

a = (0.16056/RM257mw)

b = (0.41613/HMDAmw)

c = (0.3363/EDDETmw)

d = (0.08702/PETMPmw)

print((a+b)/(c+d))