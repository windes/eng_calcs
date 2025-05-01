import streamlit as st
import math

# # Streamlit app title
# st.title("Multi-Calculator App")

# Define calculator categories and their calculators
calculators = {
    "Geometry": ["Sphere Mass Calculator", "Cylinder Volume Calculator"],
    "Thermodynamics": ["Steam Saturation Temperature Calculator"]
}

# Define calculator rendering functions
def sphere_mass_calculator():
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

    # Conversion functions
    def convert_length(value, unit):
        if unit == "micron":
            return value / 1_000_000
        elif unit == "mm":
            return value / 1000
        elif unit == "cm":
            return value / 100
        elif unit == "in":
            return value * 0.0254
        elif unit == "ft":
            return value * 0.3048
        return value

    def convert_density(value, unit):
        if unit == "g/ml":
            return value * 1000
        elif unit == "lb/in³":
            return value * 27679.90471
        elif unit == "lb/ft³":
            return value * 16.01846337
        return value

    def convert_mass(value, unit):
        if unit == "g":
            return value * 1000
        elif unit == "lb":
            return value * 2.2046226218
        return value

    # Calculate mass
    if st.button("Calculate", key="sphere_calculate"):
        if diameter <= 0 or density <= 0:
            st.error("Diameter and density must be positive values.")
        else:
            diameter_m = convert_length(diameter, diameter_unit)
            density_kg_m3 = convert_density(density, density_unit)
            radius_m = diameter_m / 2
            volume = (4/3) * math.pi * (radius_m ** 3)
            mass_kg = density_kg_m3 * volume
            mass_output = convert_mass(mass_kg, mass_unit)
            with col5:
                st.success(f"The mass of the sphere is {mass_output:.4f} {mass_unit}")

def cylinder_volume_calculator():
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

    # Conversion functions
    def convert_length(value, unit):
        if unit == "micron":
            return value / 1_000_000
        elif unit == "mm":
            return value / 1000
        elif unit == "cm":
            return value / 100
        elif unit == "in":
            return value * 0.0254
        elif unit == "ft":
            return value * 0.3048
        return value

    def convert_volume(value, unit):
        if unit == "cm³":
            return value * 1_000_000
        elif unit == "in³":
            return value * 61023.7441
        elif unit == "ft³":
            return value * 35.3146667
        return value

    # Calculate volume
    if st.button("Calculate", key="cylinder_calculate"):
        if height <= 0 or diameter_cyl <= 0:
            st.error("Height and diameter must be positive values.")
        else:
            height_m = convert_length(height, height_unit)
            diameter_m = convert_length(diameter_cyl, diameter_unit_cyl)
            radius_m = diameter_m / 2
            volume_m3 = math.pi * (radius_m ** 2) * height_m
            volume_output = convert_volume(volume_m3, volume_unit)
            with col11:
                st.success(f"The volume of the cylinder is {volume_output:.4f} {volume_unit}")

def steam_saturation_temperature_calculator():
    # LaTeX equation and nomenclature
    st.markdown("### Equation")
    st.markdown("The saturation temperature of steam is approximated using the following equation:")
    st.latex(r"T_{\text{sat}} = 100 \cdot \left( \frac{P}{0.6113} \right)^{0.25}")

    st.markdown("### Nomenclature")
    st.markdown(r"""
    - $T_{\text{sat}}$: Saturation temperature of steam (°C)  
    - $P$: Pressure (bar)
    """)

    # Define unit options (SI first, then smallest to largest)
    pressure_units = ["bar", "kPa", "atm", "psi"]
    temperature_units = ["°C", "°F", "K"]

    # Layout inputs using columns
    # Row 1: Pressure
    col13, col14 = st.columns([2, 1])
    with col13:
        pressure = st.number_input("Pressure", min_value=0.0, value=1.0, step=0.1, key="steam_pressure")
    with col14:
        pressure_unit = st.selectbox("Pressure Unit", pressure_units, index=0, key="steam_pressure_unit")

    # Row 2: Temperature output unit
    col15, col16 = st.columns([2, 1])
    with col15:
        temperature_unit = st.selectbox("Temperature Output Unit", temperature_units, index=0, key="steam_temperature_unit")

    # Conversion functions
    def convert_pressure(value, unit):
        """Convert pressure to bar."""
        if unit == "kPa":
            return value / 100  # 1 bar = 100 kPa
        elif unit == "atm":
            return value * 1.01325  # 1 atm = 1.01325 bar
        elif unit == "psi":
            return value * 0.0689476  # 1 psi = 0.0689476 bar
        return value  # bar

    def convert_temperature(value, unit):
        """Convert temperature from °C to desired unit."""
        if unit == "°F":
            return (value * 9/5) + 32  # °C to °F
        elif unit == "K":
            return value + 273.15  # °C to K
        return value  # °C

    # Calculate saturation temperature
    if st.button("Calculate", key="steam_calculate"):
        if pressure <= 0:
            st.error("Pressure must be a positive value.")
        else:
            pressure_bar = convert_pressure(pressure, pressure_unit)
            # Approximate saturation temperature in °C
            t_sat_c = 100 * (pressure_bar / 0.6113) ** 0.25
            # Ensure temperature is physically realistic (e.g., above 0°C)
            if t_sat_c < 0:
                st.error("Pressure too low for this approximation.")
            else:
                t_sat_output = convert_temperature(t_sat_c, temperature_unit)
                with col15:
                    st.success(f"The saturation temperature is {t_sat_output:.2f} {temperature_unit}")

# Map calculator names to their functions
calculator_functions = {
    "Sphere Mass Calculator": sphere_mass_calculator,
    "Cylinder Volume Calculator": cylinder_volume_calculator,
    "Steam Saturation Temperature Calculator": steam_saturation_temperature_calculator
}

# Sidebar: Search and Tree Structure
st.sidebar.header("Calculator Navigation")

# Search field
search_term = st.sidebar.text_input("Search Calculators", "").lower()

# Initialize session state for selected calculator
if "selected_calculator" not in st.session_state:
    st.session_state.selected_calculator = "Sphere Mass Calculator"  # Default to first calculator

# Filter calculators based on search term
filtered_calculators = {}
for category, calc_list in calculators.items():
    filtered_list = [calc for calc in calc_list if search_term in calc.lower()]
    if filtered_list:
        filtered_calculators[category] = filtered_list

# Display tree structure with expanders
if not filtered_calculators:
    st.sidebar.write("No calculators match your search.")
else:
    for category, calc_list in filtered_calculators.items():
        with st.sidebar.expander(category):
            # Use radio buttons to select a calculator within the category
            selected_calc = st.radio(
                f"Select a {category} calculator",
                calc_list,
                index=calc_list.index(st.session_state.selected_calculator) if st.session_state.selected_calculator in calc_list else 0,
                key=f"radio_{category}"
            )
            # Update session state when a calculator is selected
            if selected_calc:
                st.session_state.selected_calculator = selected_calc

# Main panel: Display the selected calculator
if st.session_state.selected_calculator in calculator_functions:
    calculator_functions[st.session_state.selected_calculator]()
else:
    st.write("Please select a calculator from the sidebar.")
