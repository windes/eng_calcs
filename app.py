import streamlit as st
import math

# Streamlit app title
st.title("Sphere Mass Calculator")

# LaTeX equation and nomenclature
st.markdown(r"""
### Equation
The mass of the sphere is calculated using the following equation:

\[
m = \rho \cdot \frac{4}{3} \pi \left( \frac{d}{2} \right)^3
\]

### Nomenclature
- \( m \): Mass of the sphere
- \( \rho \): Density of the sphere
- \( d \): Diameter of the sphere
""")

# Define unit options (SI first, then smallest to largest)
diameter_units = ["m", "micron", "mm", "cm", "in", "ft"]
density_units = ["kg/m³", "g/ml", "lb/in³", "lb/ft³"]
mass_units = ["kg", "g", "lb"]

# Layout inputs using columns
# Row 1: Diameter
col1, col2 = st.columns([2, 1])
with col1:
    diameter = st.number_input("Sphere Diameter", min_value=0.0, value=1.0, step=0.1)
with col2:
    diameter_unit = st.selectbox("Diameter Unit", diameter_units, index=0)

# Row 2: Density
col3, col4 = st.columns([2, 1])
with col3:
    density = st.number_input("Sphere Density", min_value=0.0, value=1000.0, step=10.0)
with col4:
    density_unit = st.selectbox("Density Unit", density_units, index=0)

# Row 3: Mass output unit
col5, col6 = st.columns([2, 1])
with col5:
    mass_unit = st.selectbox("Mass Output Unit", mass_units, index=0)

# Conversion functions
def convert_diameter(value, unit):
    """Convert diameter to meters."""
    if unit == "micron":
        return value / 1_000_000  # 1 micron = 10^-6 m
    elif unit == "mm":
        return value / 1000  # 1 mm = 10^-3 m
    elif unit == "cm":
        return value / 100  # 1 cm = 10^-2 m
    elif unit == "in":
        return value * 0.0254  # 1 in = 0.0254 m
    elif unit == "ft":
        return value * 0.3048  # 1 ft = 0.3048 m
    return value  # m

def convert_density(value, unit):
    """Convert density to kg/m³."""
    if unit == "g/ml":
        return value * 1000  # 1 g/ml = 1 g/cm³ = 1000 kg/m³
    elif unit == "lb/in³":
        return value * 27679.90471  # 1 lb/in³ = 27679.90471 kg/m³
    elif unit == "lb/ft³":
        return value * 16.01846337  # 1 lb/ft³ = 16.01846337 kg/m³
    return value  # kg/m³

def convert_mass(value, unit):
    """Convert mass from kg to desired unit."""
    if unit == "g":
        return value * 1000  # 1 kg = 1000 g
    elif unit == "lb":
        return value * 2.2046226218  # 1 kg = 2.2046226218 lb
    return value  # kg

# Calculate mass
if st.button("Calculate"):
    if diameter <= 0 or density <= 0:
        st.error("Diameter and density must be positive values.")
    else:
        # Convert inputs to SI units
        diameter_m = convert_diameter(diameter, diameter_unit)
        density_kg_m3 = convert_density(density, density_unit)

        # Calculate volume (m³)
        radius_m = diameter_m / 2
        volume = (4/3) * math.pi * (radius_m ** 3)

        # Calculate mass (kg)
        mass_kg = density_kg_m3 * volume

        # Convert mass to desired output unit
        mass_output = convert_mass(mass_kg, mass_unit)

        # Display result in the third row
        with col5:
            st.success(f"The mass of the sphere is {mass_output:.4f} {mass_unit}")
