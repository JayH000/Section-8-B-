import numpy as np
from scipy.integrate import romberg

def V(x):
    return x**4  # Potential function

def transformed_integrand(theta, a):
    x = a * np.sin(theta) ** 2  # Variable transformation
    dx_dtheta = 2 * a * np.sin(theta) * np.cos(theta)  # Jacobian term
    return (dx_dtheta / np.sqrt(V(a) - V(x)))

def compute_period_romberg(a, m=1):
    sqrt_factor = np.sqrt(8 * m)
    T = sqrt_factor * romberg(transformed_integrand, 0, np.pi/2, args=(a,))  # Integrate over transformed variable
    return T

# Test with a = 2
a = 2
T_romberg = compute_period_romberg(a)
print(f"Time period using Romberg integration for a={a}: {T_romberg}")
