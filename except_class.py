"""Custom Exception Class for Input Errors"""

class InputError(Exception):
    """Exception raised for errors in the input data."""

    def __init__(self, message):
        """Initialize the InputError with a custom error message."""
        self.message = message

    def __str__(self):
        """Return the error message as a string."""
        return self.message