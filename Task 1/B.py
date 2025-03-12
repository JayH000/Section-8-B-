#Defining without numpy 

class QuadratureMethods:
    def midpoint_rule(self, f, a, b, n):
        """
        Midpoint Rule for numerical integration.
        
        Parameters:
        - f: function to integrate
        - a: lower bound of integration
        - b: upper bound of integration
        - n: number of subintervals

        Returns:
        - Approximation of the integral using Midpoint Rule.
        """
        h = (b - a) / n  # Step size
        integral = 0

        for i in range(n):
            x_mid = a + (i + 0.5) * h  # Midpoint of the subinterval
            integral += f(x_mid)  # Evaluate function at the midpoint
        
        return h * integral

    def trapezoidal_rule(self, f, a, b, n):
        """
        Trapezoidal Rule for numerical integration.
        
        Parameters:
        - f: function to integrate
        - a: lower bound of integration
        - b: upper bound of integration
        - n: number of subintervals

        Returns:
        - Approximation of the integral using Trapezoidal Rule.
        """
        h = (b - a) / n  # Step size
        integral = 0.5 * (f(a) + f(b))  # Endpoints contribution

        for i in range(1, n):
            x = a + i * h  # Interior points
            integral += f(x)
        
        return h * integral

    def simpsons_rule(self, f, a, b, n):
        """
        Simpson's Rule for numerical integration.
        
        Parameters:
        - f: function to integrate
        - a: lower bound of integration
        - b: upper bound of integration
        - n: number of subintervals (must be even)

        Returns:
        - Approximation of the integral using Simpson's Rule.
        """
        if n % 2 == 1:
            raise ValueError("Simpson's rule requires an even number of intervals.")

        h = (b - a) / n  # Step size
        integral = f(a) + f(b)  # Endpoints contribution

        for i in range(1, n, 2):
            x = a + i * h  # Odd indices (multiplied by 4)
            integral += 4 * f(x)

        for i in range(2, n-1, 2):
            x = a + i * h  # Even indices (multiplied by 2)
            integral += 2 * f(x)
        
        return (h / 3) * integral


# Example Usage
if __name__ == "__main__":
    # Define a test function
    def test_function(x):
        return x**2  # Example: f(x) = x^2

    # Set integration limits
    a, b = 0, 1
    n = 10  # Number of subintervals

    # Create an instance of QuadratureMethods
    quadrature = QuadratureMethods()

    # Compute integrals
    midpoint_result = quadrature.midpoint_rule(test_function, a, b, n)
    trapezoidal_result = quadrature.trapezoidal_rul
