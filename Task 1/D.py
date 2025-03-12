import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

# Parent class
class Quad:
    def __init__(self, a, b):
        self.a = a  # Lower bound of integration
        self.b = b  # Upper bound of integration

# Child class inheriting from Quad
class GaussQuad(Quad):
    def __init__(self, a, b, order):
        super().__init__(a, b)  # Inherit bounds
        self.order = order  # Order of Legendre polynomial

    def legendre_polynomial(self, M, x):
        """
        Compute the Mth Legendre polynomial P_M(x) using the derivative formula.
        """
        coeff = 1 / (2**M * np.math.factorial(M))  # Prefactor
        poly = (x**2 - 1)**M  # (x^2 - 1)^M
        derivative = np.polyder(poly, M)  # Take M-th derivative
        
        return coeff * derivative

    def plot_legendre_polynomials(self, max_order=5):
        """
        Plot Legendre polynomials for orders M = [1,2,3,4,5].
        """
        x = np.linspace(-1, 1, 200)  # Define x range

        plt.figure(figsize=(8,6))
        for M in range(1, max_order + 1):
            P_M = sp.legendre(M)  # Use SciPy to get Legendre polynomial
            y = P_M(x)  # Evaluate polynomial
            
            plt.plot(x, y, label=f'P_{M}(x)')

        plt.xlabel("x")
        plt.ylabel("P_M(x)")
        plt.title("Legendre Polynomials for M = [1,2,3,4,5]")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.legend()
        plt.grid(True)
        plt.show()


# Example Usage
if __name__ == "__main__":
    # Define bounds
    a, b = -1, 1  # Standard Gauss-Legendre integration bounds

    # Create an instance of GaussQuad
    gauss_quad = GaussQuad(a, b, order=5)

    # Plot Legendre polynomials for M=[1,2,3,4,5]
    gauss_quad.plot_legendre_polynomials()
