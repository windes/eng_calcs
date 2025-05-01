import streamlit as st
import math

# Streamlit app title
st.title("Multi-Calculator App")

# Define calculator categories and their calculators
calculators = {
    "Geometry": ["Sphere Mass Calculator", "Cylinder Volume Calculator"],
    "Thermodynamics": ["Steam Saturation Temperature Calculator"],
    "Particles": ["Particle Settling Velocity Calculator"]
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
    density_units = ["kg/m³", "g/cm³", "lb/ft³"]
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
        if unit == "g/cm³":
            return value * 1000
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
        if unit == "kPa":
            return value / 100
        elif unit == "atm":
            return value * 1.01325
        elif unit == "psi":
            return value * 0.0689476
        return value

    def convert_temperature(value, unit):
        if unit == "°F":
            return (value * 9/5) + 32
        elif unit == "K":
            return value + 273.15
        return value

    # Calculate saturation temperature
    if st.button("Calculate", key="steam_calculate"):
        if pressure <= 0:
            st.error("Pressure must be a positive value.")
        else:
            pressure_bar = convert_pressure(pressure, pressure_unit)
            t_sat_c = 100 * (pressure_bar / 0.6113) ** 0.25
            if t_sat_c < 0:
                st.error("Pressure too low for this approximation.")
            else:
                t_sat_output = convert_temperature(t_sat_c, temperature_unit)
                with col15:
                    st.success(f"The saturation temperature is {t_sat_output:.2f} {temperature_unit}")

def particle_settling_velocity_calculator():
    # Title and description
    st.markdown("## Particle Settling Velocity")
    st.markdown("This tool calculates the terminal settling velocity of a spherical particle")

    # Define unit options (SI first, then smallest to largest)
    length_units = ["m", "micron", "mm", "cm", "in", "ft"]
    density_units = ["kg/m³", "g/cm³", "lb/ft³"]
    viscosity_units = ["Pa·s", "cP", "lb/ft·s"]
    time_units = ["s", "min", "hr"]
    distance_units = ["m", "cm", "ft"]
    velocity_units = ["m/s", "cm/s", "ft/s"]
    dimensionless_units = ["Dimensionless"]

    # Inputs
    # Row 1: Particle Diameter
    col1, col2 = st.columns([2, 1])
    with col1:
        diameter = st.number_input("Particle Diameter", min_value=0.0, value=0.001, step=0.0001, key="particle_diameter")
    with col2:
        diameter_unit = st.selectbox("Diameter Unit", length_units, index=0, key="particle_diameter_unit")

    # Row 2: Particle Density
    col3, col4 = st.columns([2, 1])
    with col3:
        particle_density = st.number_input("Particle Density", min_value=0.0, value=2500.0, step=10.0, key="particle_density")
    with col4:
        particle_density_unit = st.selectbox("Particle Density Unit", density_units, index=0, key="particle_density_unit")

    # Row 3: Fluid Density
    col5, col6 = st.columns([2, 1])
    with col5:
        fluid_density = st.number_input("Fluid Density", min_value=0.0, value=1000.0, step=10.0, key="fluid_density")
    with col6:
        fluid_density_unit = st.selectbox("Fluid Density Unit", density_units, index=0, key="fluid_density_unit")

    # Row 4: Fluid Viscosity
    col7, col8 = st.columns([2, 1])
    with col7:
        fluid_viscosity = st.number_input("Fluid Viscosity", min_value=0.0, value=0.001, step=0.0001, key="fluid_viscosity")
    with col8:
        fluid_viscosity_unit = st.selectbox("Fluid Viscosity Unit", viscosity_units, index=0, key="fluid_viscosity_unit")

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
        if unit == "g/cm³":
            return value * 1000
        elif unit == "lb/ft³":
            return value * 16.01846337
        return value

    def convert_viscosity(value, unit):
        if unit == "cP":
            return value / 1000  # 1 cP = 0.001 Pa·s
        elif unit == "lb/ft·s":
            return value * 1.488164  # 1 lb/ft·s = 1.488164 Pa·s
        return value

    def convert_time(value, unit):
        if unit == "min":
            return value / 60  # s to min
        elif unit == "hr":
            return value / 3600  # s to hr
        return value

    def convert_distance(value, unit):
        if unit == "cm":
            return value * 100  # m to cm
        elif unit == "ft":
            return value * 3.28084  # m to ft
        return value

    def convert_velocity(value, unit):
        if unit == "cm/s":
            return value * 100  # m/s to cm/s
        elif unit == "ft/s":
            return value * 3.28084  # m/s to ft/s
        return value

    # Outputs (non-editable text boxes with unit dropdowns)
    # Row 5: Reynolds Number
    col9, col10 = st.columns([2, 1])
    reynolds_value = st.session_state.get("particle_reynolds", "")
    with col9:
        st.text_input("Particle Reynolds Number at Terminal Velocity", value=str(reynolds_value), disabled=True, key="output_reynolds")
    with col10:
        reynolds_unit = st.selectbox("Reynolds Unit", dimensionless_units, index=0, key="reynolds_unit")

    # Row 6: Drag Coefficient
    col11, col12 = st.columns([2, 1])
    drag_coeff_value = st.session_state.get("drag_coefficient", "")
    with col11:
        st.text_input("Drag Coefficient at Terminal Velocity", value=str(drag_coeff_value), disabled=True, key="output_drag_coeff")
    with col12:
        drag_coeff_unit = st.selectbox("Drag Coefficient Unit", dimensionless_units, index=0, key="drag_coeff_unit")

    # Row 7: Time to Terminal Velocity
    col13, col14 = st.columns([2, 1])
    time_value = st.session_state.get("time_to_terminal", "")
    with col13:
        st.text_input("Time to Accelerate to Terminal Velocity", value=str(time_value), disabled=True, key="output_time")
    with col14:
        time_unit = st.selectbox("Time Unit", time_units, index=0, key="time_unit")

    # Row 8: Distance Fallen
    col15, col16 = st.columns([2, 1])
    distance_value = st.session_state.get("distance_to_terminal", "")
    with col15:
        st.text_input("Distance Fallen to Reach Terminal Velocity", value=str(distance_value), disabled=True, key="output_distance")
    with col16:
        distance_unit = st.selectbox("Distance Unit", distance_units, index=0, key="distance_unit")

    # Row 9: Terminal Velocity
    col17, col18 = st.columns([2, 1])
    velocity_value = st.session_state.get("terminal_velocity", "")
    with col17:
        st.text_input("Terminal Velocity", value=str(velocity_value), disabled=True, key="output_velocity")
    with col18:
        velocity_unit = st.selectbox("Velocity Unit", velocity_units, index=0, key="velocity_unit")

    # Calculate terminal velocity
    if st.button("Calculate", key="particle_calculate"):
        if diameter <= 0 or particle_density <= 0 or fluid_density <= 0 or fluid_viscosity <= 0:
            st.error("All inputs must be positive values.")
        elif particle_density <= fluid_density:
            st.error("Particle density must be greater than fluid density for the particle to settle.")
        else:
            # Convert inputs to SI units
            d_m = convert_length(diameter, diameter_unit)
            rho_p = convert_density(particle_density, particle_density_unit)
            rho_f = convert_density(fluid_density, fluid_density_unit)
            mu = convert_viscosity(fluid_viscosity, fluid_viscosity_unit)

            # Constants
            g = 9.81  # gravitational acceleration (m/s²)
            dt = 0.001  # time step (s)
            epsilon = 1e-6  # convergence criterion for velocity (m/s)

            # Particle properties
            volume = (4/3) * math.pi * (d_m / 2) ** 3
            mass = rho_p * volume

            # Forces
            F_g = mass * g  # weight force
            F_b = rho_f * volume * g  # buoyancy force
            F_net_grav = F_g - F_b  # net gravitational force

            # Simulation loop
            v = 1e-12  # initial velocity (m/s)
            z = 0  # initial position (m)
            t = 0  # initial time (s)
            while True:
                # Calculate Reynolds number
                Re_p = (rho_f * v * d_m) / mu if mu > 0 else 0

                # Calculate drag coefficient (piecewise correlation)
                if Re_p < 0.1:
                    C_D = 24 / Re_p if Re_p > 0 else 0  # Stokes' Law
                elif Re_p < 1000:
                    C_D = (24 / Re_p) * (1 + 0.15 * Re_p ** 0.687)  # Intermediate regime
                else:
                    C_D = 0.44  # Newton's regime

                # Calculate drag force
                F_d = 0.5 * rho_f * v ** 2 * C_D * math.pi * (d_m / 2) ** 2

                # Net force and acceleration
                F_net = F_net_grav - F_d  # drag opposes gravity
                a = F_net / mass if mass > 0 else 0

                # Update velocity and position
                v_new = v + a * dt
                z += v * dt
                t += dt

                # Check for convergence
                if abs(v_new - v) < epsilon:
                    break

                v = v_new

            # Store results in session state for display
            st.session_state.particle_reynolds = f"{Re_p:.4f}"
            st.session_state.drag_coefficient = f"{C_D:.4f}"
            st.session_state.time_to_terminal = f"{convert_time(t, time_unit):.4f}"
            st.session_state.distance_to_terminal = f"{convert_distance(z, distance_unit):.4f}"
            st.session_state.terminal_velocity = f"{convert_velocity(v, velocity_unit):.4f}"

            # Force re-render to update output fields
            st.rerun()

# Map calculator names to their functions
calculator_functions = {
    "Sphere Mass Calculator": sphere_mass_calculator,
    "Cylinder Volume Calculator": cylinder_volume_calculator,
    "Steam Saturation Temperature Calculator": steam_saturation_temperature_calculator,
    "Particle Settling Velocity Calculator": particle_settling_velocity_calculator
}

# Sidebar: Search and Tree Structure
st.sidebar.header("Calculator Navigation")

# Search field
search_term = st.sidebar.text_input("Search Calculators", "").lower()

# Clear selection button
if st.sidebar.button("Clear Selection"):
    st.session_state.selected_calculator = None

# Initialize session state for selected calculator
if "selected_calculator" not in st.session_state:
    st.session_state.selected_calculator = None

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
            for calc in calc_list:
                # Use a button for each calculator
                if st.button(calc, key=f"button_{calc}"):
                    # Toggle selection: if already selected, deselect; otherwise, select
                    if st.session_state.selected_calculator == calc:
                        st.session_state.selected_calculator = None
                    else:
                        st.session_state.selected_calculator = calc

# Main panel: Display the selected calculator
if st.session_state.selected_calculator and st.session_state.selected_calculator in calculator_functions:
    calculator_functions[st.session_state.selected_calculator]()
else:
    st.write("Please select a calculator from the sidebar.")
