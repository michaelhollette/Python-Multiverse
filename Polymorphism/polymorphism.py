
# Polymorphism in Python

# 1. Function Polymorphism
# Function polymorphism allows functions to handle arguments of different types flexibly.
# For example, using the built-in `len()` function on different types of objects.

print("1. Function Polymorphism Example")

# The len() function can work on various iterable types, such as strings, lists, and dictionaries.
print(len("hello"))  # String: Outputs 5
print(len([1, 2, 3, 4]))  # List: Outputs 4
print(len({"key1": "value1", "key2": "value2"}))  # Dictionary: Outputs 2

# Here, the `len()` function behaves differently depending on the object type, demonstrating function polymorphism.

print("\n")


# 2. Class Polymorphism
# Class polymorphism allows objects of different classes to be used interchangeably if they implement a common interface.
# Python achieves this through "duck typing," meaning "if it walks like a duck and quacks like a duck, it is a duck."

print("2. Class Polymorphism Example")

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

class Duck:
    def sound(self):
        return "Quack"

# Function that can accept any object with a `sound` method
def animal_sound(animal):
    return animal.sound()

# Instances of different classes
animals = [Cat(), Dog(), Duck()]

# Using class polymorphism to call `sound` on different animal types
for animal in animals:
    print(animal_sound(animal))

# Here, despite `Cat`, `Dog`, and `Duck` being different classes, they are used interchangeably based on their `sound` method.
# This is class polymorphism in action.

print("\n")


# 3. Inheritance Polymorphism
# Inheritance polymorphism allows a subclass to override a method from a parent class,
# allowing each subclass to implement the method differently.

print("3. Inheritance Polymorphism Example")

class Animal:
    def speak(self):
        return "Some generic sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Bark"

# List of animals of different types
animals = [Animal(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

# Here, the `speak` method is polymorphic. When called on `Cat` or `Dog` objects, it invokes the overridden method,
# demonstrating inheritance polymorphism.

print("\n")

# Conclusion:
# - Function polymorphism lets us use functions like `len()` on different types.
# - Class polymorphism lets us pass different types of objects to a function, as long as they provide a compatible interface.
# - Inheritance polymorphism lets us define common behavior in a parent class, with subclasses providing specific implementations.

# Save and run this script to see polymorphism examples in action.
