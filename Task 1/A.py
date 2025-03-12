import numpy as np

class QuadratureMethods:
    def __init__(self, func, a, b):
        """
        Initialize the quadrature methods class.

        Parameters:
        - func: function to integrate
        - a: lower bound of integration
        - b: upper bound of integration
        """
        self.func = func
        self.a = a
        self.b = b

    def midpoint_rule(self):
        """Apply the Midpoint Rule."""
        midpoint = (self.a + self.b) / 2
        return (self.b - self.a) * self.func(midpoint)

    def trapezoidal_rule(self):
        """Apply the Trapezoidal Rule."""
        return (self.b - self.a) / 2 * (self.func(self.a) + self.func(self.b))

    def simpsons_rule(self):
        """Apply Simpson’s Rule."""
        midpoint = (self.a + self.b) / 2
        return (self.b - self.a) / 6 * (self.func(self.a) + 4 * self.func(midpoint) + self.func(self.b))

# Example usage
if __name__ == "__main__":
    # Define a test function
    def test_function(x):
        return np.exp(-x**2)  # Example: Gaussian function

    # Set integration limits
    a, b = 0, 1

    # Create an instance of QuadratureMethods
    quadrature = QuadratureMethods(test_function, a, b)

    # Compute the integral using different methods
    midpoint_result = quadrature.midpoint_rule()
    trapezoidal_result = quadrature.trapezoidal_rule()
    simpsons_result = quadrature.simpsons_rule()

    # Print results
    print(f"Midpoint Rule Approximation: {midpoint_result}")
    print(f"Trapezoidal Rule Approximation: {trapezoidal_result}")
    print(f"Simpson’s Rule Approximation: {simpsons_result}")
