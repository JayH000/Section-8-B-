import numpy as np
import scipy.integrate as spi

def oscillator_period(a):
    
    integrand = lambda x: 1 / np.sqrt(a**4 - x**4)
    integral, _ = spi.quad(integrand, 0, a)
    
    return np.sqrt(8) * integral

# Example usage:
amplitude = 1.0
T = oscillator_period(amplitude)
print(f"Period for amplitude {amplitude}: {T}")
