import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.special as sp

# Define quadrature methods
def midpoint_rule(f, a, b, N):
    """Midpoint rule for numerical integration."""
    h = (b - a) / N
    x_mid = a + h * (np.arange(N) + 0.5)
    return h * np.sum(f(x_mid))

def trapezoidal_rule(f, a, b, N):
    """Trapezoidal rule for numerical integration."""
    x = np.linspace(a, b, N+1)
    y = f(x)
    return (b - a) / (2 * N) * (y[0] + 2*np.sum(y[1:-1]) + y[-1])

def simpsons_rule(f, a, b, N):
    """Simpson’s rule for numerical integration (N must be even)."""
    if N % 2 == 1:  
        N += 1  # Ensure even number of intervals
    x = np.linspace(a, b, N+1)
    y = f(x)
    h = (b - a) / N
    return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def gauss_legendre_quadrature(f, a, b, M):
    """Gauss-Legendre quadrature with M points."""
    x, w = sp.roots_legendre(M)  # Get nodes and weights
    x_mapped = 0.5 * (b - a) * x + 0.5 * (b + a)  # Map to [a, b]
    return 0.5 * (b - a) * np.sum(w * f(x_mapped))

# Compute relative errors for heatmap
k_values = np.arange(0, 11)
N_values = np.logspace(1, 5, num=20, dtype=int)
methods = ["Midpoint", "Trapezoidal", "Simpson", "Gauss-Legendre"]
errors = {method: np.zeros((len(k_values), len(N_values))) for method in methods}

for i, k in enumerate(k_values):
    f_k = lambda x: x**k  # Define polynomial function
    I_true = 1 / (k + 1)   # Exact integral value

    for j, N in enumerate(N_values):
        M = min(N, 20)  # Use reasonable number of points for Gauss Quadrature
        
        # Compute quadrature results
        M_k = midpoint_rule(f_k, 0, 1, N)
        T_k = trapezoidal_rule(f_k, 0, 1, N)
        S_k = simpsons_rule(f_k, 0, 1, N)
        G_k = gauss_legendre_quadrature(f_k, 0, 1, M)

        # Compute relative errors
        errors["Midpoint"][i, j] = (2 * I_true - M_k) / (I_true + M_k)
        errors["Trapezoidal"][i, j] = (2 * I_true - T_k) / (I_true + T_k)
        errors["Simpson"][i, j] = (2 * I_true - S_k) / (I_true + S_k)
        errors["Gauss-Legendre"][i, j] = (2 * I_true - G_k) / (I_true + G_k)

# Plot heatmaps
plt.figure(figsize=(12, 10))
for i, method in enumerate(methods):
    plt.subplot(2, 2, i+1)
    sns.heatmap(errors[method], xticklabels=np.log10(N_values).astype(int), yticklabels=k_values, cmap="coolwarm", annot=False)
    plt.xlabel("log10(N)")
    plt.ylabel("Polynomial Order k")
    plt.title(f"Relative Error - {method}")

plt.tight_layout()
plt.show()
