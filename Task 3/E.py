import numpy as np
from scipy.integrate import romberg

# Define the potential function V(x) = x^4
def integrand(x, a):
    return 1 / np.sqrt(a**4 - x**4)

# Function to compute the time period
def compute_period(a, show=True):
    # Factor outside the integral
    prefactor = np.sqrt(8)

    # Compute the integral using Romberg's method
    T = prefactor * romberg(integrand, 0, a, args=(a,), show=show, divmax=10)

    return T

# Compute period for a = 2 with detailed output
T_a2 = compute_period(2, show=True)
print(f"\nEstimated Time Period for a=2: {T_a2}")
