"""
Custom Exceptions
"""

class NonPositiveInputError(Exception):
    """Exception raised when input is non-positive (>=0)
    
    Attributes:
        value -- entered value
        message -- explanation of why input must be greater than 0
    """
    def __init__(self, value, message):
        self.value = value
        self.message = message

class NegativeInputError(Exception):
    """Exception raised when input is non-positive (>=0)
    
    Attributes:
        value -- entered value
        message -- explanation of why input must be positive
    """    
    def __init__(self, value, message):
        self.value = value
        self.message = message
        

class InvalidFilter(Exception):
    """Exception raised when desired filter is not available or misspelled
    
    Attributes:
        value -- entered value
        message -- explanation of why input is not valid
    """    
    def __init__(self, value, message):
        self.value = value
        self.message = message
