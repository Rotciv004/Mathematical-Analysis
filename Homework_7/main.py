import numpy as np

def integrate(func, a, b, num_intervals):
    """Numerical integration using the trapezoidal rule."""
    x = np.linspace(a, b, num_intervals + 1)
    y = func(x)
    h = (b - a) / num_intervals
    integral = h * (0.5 * y[0] + 0.5 * y[-1] + np.sum(y[1:-1]))
    return integral

# Define the function e^(-x^2)
def gaussian(x):
    return np.exp(-x**2)

# Set a range of values for a
a_values = np.arange(0.1, 5.1, 0.1)

# Calculate the integral for each value of a
for a in a_values:
    result = integrate(gaussian, -a, a, 1000)
    print(f"For a = {a}, integral ≈ {result}, π ≈ {np.sqrt(np.pi)}")
