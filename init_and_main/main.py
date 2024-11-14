# main.py

from math_tools import add, subtract

def main():
    """Main function that runs a demo of math operations."""
    print("Running main program")
    print("Addition of 10 + 5:", add(10, 5))
    print("Subtraction of 10 - 3:", subtract(10, 3))

# Code that runs only when main.py is executed directly
if __name__ == "__main__":
    main()
