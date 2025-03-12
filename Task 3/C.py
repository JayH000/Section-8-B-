import numpy as np
from scipy.integrate import fixed_quad, quad

def potential(x):
    return x**4

def integrand(x, a):
    return 1 / np.sqrt(potential(a) - potential(x))

def compute_time_period_fixed_quad(a, N):
    integral, _ = fixed_quad(integrand, 0, a, args=(a,), n=N)
    return np.sqrt(8) * integral

def compute_time_period_quad(a):
    integral, error = quad(integrand, 0, a, args=(a,))
    return np.sqrt(8) * integral, error

a = 2
N_values = [2**i for i in range(1, 11)]
errors = []

for N in N_values:
    T_N = compute_time_period_fixed_quad(a, N)
    T_2N = compute_time_period_fixed_quad(a, 2*N)
    error = abs(T_2N - T_N)
    errors.append(error)
    if error < 1e-4:
        print(f'Minimum N for error < 1e-4: {N}')
        break

T_quad, quad_error = compute_time_period_quad(a)
print(f'Time period using quad: {T_quad}, Estimated error: {quad_error}')
