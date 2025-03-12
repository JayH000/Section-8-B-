import numpy as np
import matplotlib.pyplot as plt
from scipy.special import roots_legendre

# Define the Fermi-Dirac function
def fermi_dirac(x, k):
    return 1 / (1 + np.exp(-k * x))

# True integral for Fermi-Dirac distribution
def true_integral(a, b, k):
    return (1 / k) * (np.log(np.exp(k * b) + 1) - np.log(np.exp(k * a) + 1))

# Midpoint Rule
def midpoint_rule(f, a, b, N, k):
    h = (b - a) / N
    return h * np.sum(f(a + (np.arange(N) + 0.5) * h, k))

# Trapezoidal Rule
def trapezoidal_rule(f, a, b, N, k):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    return (h / 2) * (f(x[0], k) + 2 * np.sum(f(x[1:-1], k)) + f(x[-1], k))

# Simpson's Rule
def simpsons_rule(f, a, b, N, k):
    if N % 2 == 1:
        N += 1  # Ensure N is even
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    return (h / 3) * (f(x[0], k) + 4 * np.sum(f(x[1:-1:2], k)) + 2 * np.sum(f(x[2:-2:2], k)) + f(x[-1], k))

# Gauss-Legendre Quadrature
def gauss_legendre_rule(f, a, b, N, k):
    x, w = roots_legendre(N)
    x_mapped = 0.5 * (b - a) * x + 0.5 * (b + a)
    return 0.5 * (b - a) * np.sum(w * f(x_mapped, k))

# Compute the relative errors
def relative_error(I_true, I_quad):
    return np.abs(2 * I_true - I_quad) / np.abs(I_true + I_quad)

# Define parameters
a, b = 0, 1
k_values = np.arange(0, 11)
N_values = np.logspace(1, 5, 50, dtype=int)

# Compute errors
errors = {"Midpoint": [], "Trapezoidal": [], "Simpson": [], "Gauss-Legendre": []}
for k in k_values:
    I_true = true_integral(a, b, k)
    errors_mid, errors_trapz, errors_simps, errors_gauss = [], [], [], []
    
    for N in N_values:
        errors_mid.append(relative_error(I_true, midpoint_rule(fermi_dirac, a, b, N, k)))
        errors_trapz.append(relative_error(I_true, trapezoidal_rule(fermi_dirac, a, b, N, k)))
        errors_simps.append(relative_error(I_true, simpsons_rule(fermi_dirac, a, b, N, k)))
        errors_gauss.append(relative_error(I_true, gauss_legendre_rule(fermi_dirac, a, b, N, k)))
    
    errors["Midpoint"].append(errors_mid)
    errors["Trapezoidal"].append(errors_trapz)
    errors["Simpson"].append(errors_simps)
    errors["Gauss-Legendre"].append(errors_gauss)

# Plot heatmaps
def plot_heatmap(error_matrix, title):
    plt.figure(figsize=(8, 6))
    plt.imshow(error_matrix, aspect='auto', cmap='viridis', origin='lower',
               extent=[np.log10(N_values[0]), np.log10(N_values[-1]), k_values[0], k_values[-1]])
    plt.colorbar(label='Relative Error')
    plt.xlabel('log10(N)')
    plt.ylabel('k')
    plt.title(title)
    plt.show()

for method, error_matrix in errors.items():
    plot_heatmap(error_matrix, f'Relative Error Heatmap: {method} Rule')

