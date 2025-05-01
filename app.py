import streamlit as st
import math

# Streamlit app title
st.title("Sphere Mass Calculator")

# Define unit options
diameter_units = ["meters (m)", "centimeters (cm)", "millimeters (mm)"]
density_units = ["kg/m³", "g/cm³"]
mass_units = ["kilograms (kg)", "grams (g)"]

# Layout inputs in columns for better UI
col1, col2 = st.columns(2)

# Diameter input and unit selection
with col1:
    diameter = st.number_input("Sphere Diameter", min_value=0.0, value=1.0, step=0.1)
    diameter_unit = st.selectbox("Diameter Unit", diameter_units)

# Density input and unit selection
with col2:
    density = st.number_input("Sphere Density", min_value=0.0, value=1000.0, step=10.0)
    density_unit = st.selectbox("Density Unit", density_units)

# Mass unit selection
mass_unit = st.selectbox("Mass Output Unit", mass_units)

# Conversion functions
def convert_diameter(value, unit):
    """Convert diameter to meters."""
    if unit == "centimeters (cm)":
        return value / 100
    elif unit == "millimeters (mm)":
        return value / 1000
    return value  # meters

def convert_density(value, unit):
    """Convert density to kg/m³."""
    if unit == "g/cm³":
        return value * 1000  # 1 g/cm³ = 1000 kg/m³
    return value  # kg/m³

def convert_mass(value, unit):
    """Convert mass from kg to desired unit."""
    if unit == "grams (g)":
        return value * 1000  # 1 kg = 1000 g
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

        # Display result
        st.success(f"The mass of the sphere is {mass_output:.4f} {mass_unit}")
