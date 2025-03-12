import numpy as np
from scipy.integrate import fixed_quad

def time_period(a, N):
    V = lambda x: x**4  # Potential function V(x) = x^4
    integrand = lambda x: 1 / np.sqrt(V(a) - V(x))
    integral, _ = fixed_quad(integrand, 0, a, n=N)
    return np.sqrt(8) * integral

a = 2
N_values = [2**i for i in range(1, 11)]  # Testing different N values
errors = []

for N in N_values:
    T_N = time_period(a, N)
    T_2N = time_period(a, 2 * N)
    error = abs(T_2N - T_N)
    errors.append(error)
    print(f'N={N}, T={T_N:.6f}, Error={error:.6e}')

# Find the smallest N where error < 10^-4
for N, err in zip(N_values, errors):
    if err < 1e-4:
        print(f'Minimum N for error < 10^-4: {N}')
        break