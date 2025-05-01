import streamlit as st
import math

# Streamlit app title
st.title("Multi-Calculator App")

# Create tabs for the two calculators
tab1, tab2 = st.tabs(["Sphere Mass Calculator", "Cylinder Volume Calculator"])

# Shared conversion functions for length (used by both calculators)
def convert_length(value, unit):
    """Convert length to meters."""
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

# Tab 1: Sphere Mass Calculator
with tab1:
    # LaTeX equation and nomenclature
    st.markdown("### Equation")
    st.markdown("The mass of the sphere is calculated using the following equation:")
    st.latex(r"m = \rho \cdot \frac{4}{3} \pi \left( \frac{d}{2} \right)^3")

    st.markdown("### Nomenclature")
    st.markdown(r"""
    - $m$: Mass of the sphere  
    - $\rho$: Density of the sphere  
    - $d$: Diameter of the sphere
    """)

    # Define unit options (SI first, then smallest to largest)
    diameter_units = ["m", "micron", "mm", "cm", "in", "ft"]
    density_units = ["kg/m³", "g/ml", "lb/in³", "lb/ft³"]
    mass_units = ["kg", "g", "lb"]

    # Layout inputs using columns
    # Row 1: Diameter
    col1, col2 = st.columns([2, 1])
    with col1:
        diameter = st.number_input("Sphere Diameter", min_value=0.0, value=1.0, step=0.1, key="sphere_diameter")
    with col2:
        diameter_unit = st.selectbox("Diameter Unit", diameter_units, index=0, key="sphere_diameter_unit")

    # Row 2: Density
    col3, col4 = st.columns([2, 1])
    with col3:
        density = st.number_input("Sphere Density", min_value=0.0, value=1000.0, step=10.0, key="sphere_density")
    with col4:
        density_unit = st.selectbox("Density Unit", density_units, index=0, key="sphere_density_unit")

    # Row 3: Mass output unit
    col5, col6 = st.columns([2, 1])
    with col5:
        mass_unit = st.selectbox("Mass Output Unit", mass_units, index=0, key="sphere_mass_unit")

    # Conversion functions for density and mass
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
    if st.button("Calculate", key="sphere_calculate"):
        if diameter <= 0 or density <= 0:
            st.error("Diameter and density must be positive values.")
        else:
            # Convert inputs to SI units
            diameter_m = convert_length(diameter, diameter_unit)
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

# Tab 2: Cylinder Volume Calculator
with tab2:
    # LaTeX equation and nomenclature
    st.markdown("### Equation")
    st.markdown("The volume of the cylinder is calculated using the following equation:")
    st.latex(r"V = \pi \left( \frac{d}{2} \right)^2 h")

    st.markdown("### Nomenclature")
    st.markdown(r"""
    - $V$: Volume of the cylinder  
    - $d$: Diameter of the cylinder  
    - $h$: Height of the cylinder
    """)

    # Define unit options (SI first, then smallest to largest)
    length_units = ["m", "micron", "mm", "cm", "in", "ft"]
    volume_units = ["m³", "cm³", "in³", "ft³"]

    # Layout inputs using columns
    # Row 1: Height
    col7, col8 = st.columns([2, 1])
    with col7:
        height = st.number_input("Cylinder Height", min_value=0.0, value=1.0, step=0.1, key="cylinder_height")
    with col8:
        height_unit = st.selectbox("Height Unit", length_units, index=0, key="cylinder_height_unit")

    # Row 2: Diameter
    col9, col10 = st.columns([2, 1])
    with col9:
        diameter_cyl = st.number_input("Cylinder Diameter", min_value=0.0, value=1.0, step=0.1, key="cylinder_diameter")
    with col10:
        diameter_unit_cyl = st.selectbox("Diameter Unit", length_units, index=0, key="cylinder_diameter_unit")

    # Row 3: Volume output unit
    col11, col12 = st.columns([2, 1])
    with col11:
        volume_unit = st.selectbox("Volume Output Unit", volume_units, index=0, key="cylinder_volume_unit")

    # Conversion function for volume
    def convert_volume(value, unit):
        """Convert volume from m³ to desired unit."""
        if unit == "cm³":
            return value * 1_000_000  # 1 m³ = 10^6 cm³
        elif unit == "in³":
            return value * 61023.7441  # 1 m³ = 61023.7441 in³
        elif unit == "ft³":
            return value * 35.3146667  # 1 m³ = 35.3146667 ft³
        return value  # m³

    # Calculate volume
    if st.button("Calculate", key="cylinder_calculate"):
        if height <= 0 or diameter_cyl <= 0:
            st.error("Height and diameter must be positive values.")
        else:
            # Convert inputs to SI units
            height_m = convert_length(height, height_unit)
            diameter_m = convert_length(diameter_cyl, diameter_unit_cyl)

            # Calculate volume (m³)
            radius_m = diameter_m / 2
            volume_m3 = math.pi * (radius_m ** 2) * height_m

            # Convert volume to desired output unit
            volume_output = convert_volume(volume_m3, volume_unit)

            # Display result in the third row
            with col11:
                st.success(f"The volume of the cylinder is {volume_output:.4f} {volume_unit}")
