import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import romberg

# Define the potential function V(x) = x^4
def integrand(x, a):
    return 1 / np.sqrt(a**4 - x**4)

# Function to compute the time period
def compute_period(a, divmax=15):
    if a == 0:
        return 0  # Avoid division errors
    prefactor = np.sqrt(8)
    return prefactor * romberg(integrand, 0, a, args=(a,), divmax=divmax)

# Generate amplitude values
a_values = np.linspace(0.01, 2, 100)  # Avoid zero for numerical stability
T_values = [compute_period(a) for a in a_values]

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(a_values, T_values, label="Time Period", color="b")
plt.xlabel("Amplitude (a)")
plt.ylabel("Time Period (T)")
plt.title("Time Period vs. Amplitude for V(x) = x^4")
plt.legend()
plt.grid()
plt.show()
