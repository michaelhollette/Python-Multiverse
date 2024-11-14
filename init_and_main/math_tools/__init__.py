# math_tools/__init__.py

# Import specific functions from submodules
from .addition import add
from .subtraction import subtract

# Define what should be imported when using 'from math_tools import *'
__all__ = ['add', 'subtract']

# Optional: Any package-level initialization code
print("math_tools package is being initialized")
