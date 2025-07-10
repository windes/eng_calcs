import streamlit as st
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objects as go

st.title("Data Regression App")

uploaded_file = st.file_uploader("Upload a CSV file with two columns (independent and dependent variables)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if df.shape[1] != 2:
        st.error("The CSV file must have exactly two columns.")
    else:
        x_col, y_col = df.columns
        x = df[x_col].values
        y = df[y_col].values

        model_options = [
            "Linear", "Quadratic", "Cubic",
            "Power Law", "Exponential", "Logarithmic"
        ]
        selected_model = st.selectbox("Select the equation form", model_options)

        # Define fitting functions
        def linear_func(x, a, b):
            return a * x + b

        def quadratic_func(x, a, b, c):
            return a * x**2 + b * x + c

        def cubic_func(x, a, b, c, d):
            return a * x**3 + b * x**2 + c * x + d

        def power_law_func(x, a, b):
            return a * x**b

        def exponential_func(x, a, b):
            return a * np.exp(b * x)

        def logarithmic_func(x, a, b):
            return a + b * np.log(x)

        # Mapping of models to functions and LaTeX bases
        model_map = {
            "Linear": (linear_func, r"y = ax + b", [1.0, 1.0], True),
            "Quadratic": (quadratic_func, r"y = ax^2 + bx + c", [1.0, 1.0, 1.0], True),
            "Cubic": (cubic_func, r"y = ax^3 + bx^2 + cx + d", [1.0, 1.0, 1.0, 1.0], True),
            "Power Law": (power_law_func, r"y = a x^{b}", [1.0, 1.0], False),
            "Exponential": (exponential_func, r"y = a e^{bx}", [1.0, 0.1], False),
            "Logarithmic": (logarithmic_func, r"y = a + b \ln(x)", [1.0, 1.0], False)
        }

        func, latex_base, p0, use_polyfit = model_map[selected_model]

        try:
            if use_polyfit:
                # Use np.polyfit for polynomials
                degree = len(p0) - 1
                coeffs = np.polyfit(x, y, degree)
                y_fit = np.polyval(coeffs, x)
                # Build LaTeX equation
                terms = []
                for i, coeff in enumerate(coeffs):
                    if coeff != 0:
                        power = degree - i
                        if power == 0:
                            terms.append(f"{coeff:.4f}")
                        elif power == 1:
                            terms.append(f"{coeff:.4f}x")
                        else:
                            terms.append(f"{coeff:.4f}x^{{{power}}}")
                latex_eq = r"y = " + " + ".join(terms).replace("+ -", "- ")
            else:
                # Use curve_fit for non-linear models
                popt, _ = curve_fit(func, x, y, p0=p0)
                y_fit = func(x, *popt)
                # Build LaTeX equation
                params = [f"{param:.4f}" for param in popt]
                if selected_model == "Power Law":
                    latex_eq = r"y = " + params[0] + r" x^{" + params[1] + r"}"
                elif selected_model == "Exponential":
                    latex_eq = r"y = " + params[0] + r" e^{" + params[1] + r"x}"
                elif selected_model == "Logarithmic":
                    latex_eq = r"y = " + params[0] + r" + " + params[1] + r" \ln(x)"
                else:
                    latex_eq = latex_base  # Fallback

            # Calculate R^2
            ss_res = np.sum((y - y_fit)**2)
            ss_tot = np.sum((y - np.mean(y))**2)
            r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0

            # Prepare plot
            # Sort for smooth line
            sort_idx = np.argsort(x)
            x_sorted = x[sort_idx]
            y_fit_sorted = y_fit[sort_idx]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Raw Data'))
            fig.add_trace(go.Scatter(x=x_sorted, y=y_fit_sorted, mode='lines', name='Fitted Curve'))
            fig.update_layout(title='Data and Fitted Curve', xaxis_title=x_col, yaxis_title=y_col)

            st.plotly_chart(fig)

            st.latex(latex_eq)
            st.write(f"R²: {r2:.4f}")

        except Exception as e:
            st.error(f"Error fitting the model: {str(e)}")
            st.write("Please ensure the data is suitable for the selected model (e.g., positive x for log/power).")
