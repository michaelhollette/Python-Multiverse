# encapsulation_example.py

"""
Encapsulation in Python

Encapsulation is a fundamental concept in object-oriented programming (OOP) that restricts access to certain 
attributes and methods within a class. It allows us to bundle data and the methods that operate on that data 
within a single unit, known as a class.

In Python, encapsulation is implemented through conventions and mechanisms such as single and double underscores.

Key Points:
- Encapsulation helps protect the integrity of data.
- It restricts access to specific attributes and methods from outside the class.
- Python uses a convention with underscores to indicate the privacy level of attributes and methods.

There are three main types of attributes:
    1. Public attributes
    2. Protected attributes
    3. Private attributes

Below are examples demonstrating each of these.
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make          # Public attribute
        self._model = model        # Protected attribute
        self.__year = year         # Private attribute

    def get_year(self):
        """Getter method for private attribute __year."""
        return self.__year

    def set_year(self, year):
        """Setter method for private attribute __year with validation."""
        if year > 1885:  # The first car was invented around 1885
            self.__year = year
        else:
            print("Invalid year. The car's year cannot be before 1885.")

    def display_info(self):
        """Displays information about the car."""
        print(f"Make: {self.make}, Model: {self._model}, Year: {self.__year}")

# Public attribute
"""
Public attributes are accessible from outside the class and do not have any underscore prefix.
These attributes can be read or modified freely.
"""
car = Car("Toyota", "Camry", 2020)
print("Public attribute (make):", car.make)  # Output: Toyota

# Protected attribute
"""
Protected attributes have a single underscore prefix (_) and are intended for internal use within the class 
or subclasses. However, they can still be accessed directly if needed.
"""
print("Protected attribute (model):", car._model)  # Output: Camry

# Private attribute
"""
Private attributes have a double underscore prefix (__), which triggers name mangling in Python. 
These attributes cannot be accessed directly from outside the class, as their names are modified to 
include the class name as a prefix.
"""
# Accessing private attribute directly will raise an error
try:
    print("Private attribute (year):", car.__year)  # This will raise an AttributeError
except AttributeError:
    print("Private attribute (year) cannot be accessed directly!")

# Accessing private attribute with getter method
"""
Private attributes can be accessed or modified through getter and setter methods.
"""
print("Private attribute accessed via getter method:", car.get_year())  # Output: 2020

# Setting private attribute with setter method
car.set_year(2022)
print("Updated year via setter method:", car.get_year())  # Output: 2022

# Attempting to set an invalid year
car.set_year(1800)  # Output: Invalid year. The car's year cannot be before 1885.

"""
Summary:
- Public attributes: Accessible freely from outside the class.
- Protected attributes (_): Intended for internal use, but still accessible if needed.
- Private attributes (__): Intended to be hidden, with access only through getter/setter methods.

Encapsulation allows us to protect data by controlling how it can be accessed or modified. 
This helps maintain the integrity of an object’s state and promotes clean, modular code.
"""

# Running the display_info method to see all details of the car
car.display_info()  # Output: Make: Toyota, Model: Camry, Year: 2022
