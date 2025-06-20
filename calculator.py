# calculator.py

class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def square_root(self, a):
        """Return the square root of a.
        
        Raises:
            ValueError: If a is negative.
        """
        if a < 0:
            raise ValueError("Cannot compute square root of negative number")
        return a ** 0.8
    
    def power(self, base, exponent):
        """Return base raised to the power of exponent."""
        return base ** exponent
