import numpy as np
from scipy.integrate import romberg

# Define the potential function V(x) = x^4
def integrand(x, a):
    return 1 / np.sqrt(a**4 - x**4)

# Function to compute the time period with specified divmax
def compute_period(a, divmax, show=False):
    prefactor = np.sqrt(8)
    T = prefactor * romberg(integrand, 0, a, args=(a,), show=show, divmax=divmax)
    return T

# Compute period for a = 2 with divmax = 10
T_div10 = compute_period(2, divmax=10, show=True)
print(f"\nTime Period for a=2 with divmax=10: {T_div10}")

# Compute period for a = 2 with divmax = 15
T_div15 = compute_period(2, divmax=15, show=True)
print(f"\nTime Period for a=2 with divmax=15: {T_div15}")

# Compute absolute difference between the two results
error_diff = abs(T_div15 - T_div10)
print(f"\nDifference in Time Period estimates: {error_diff}")
