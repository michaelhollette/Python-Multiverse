# unit_test_guide.py

# Import the unittest module
import unittest

# Example function to be tested
def add(a, b):
    """Returns the sum of a and b"""
    return a + b

# Unit Test Class for the add function
class TestAddFunction(unittest.TestCase):
    
    # Basic test case: Adding positive numbers
    def test_add_positive(self):
        self.assertEqual(add(3, 4), 7)  # Expected output: 7
    
    # Test case: Adding negative numbers
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)  # Expected output: -2
    
    # Test case: Adding zero
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)  # Expected output: 5

    # Test for exceptions
    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            add("a", 1)  # Adding string and int should raise TypeError

# Setup and Teardown example (if needed)
class TestWithSetup(unittest.TestCase):

    def setUp(self):
        """Code to run before each test"""
        self.a = 5
        self.b = 10

    def tearDown(self):
        """Code to run after each test"""
        del self.a
        del self.b

    def test_add_setup(self):
        self.assertEqual(add(self.a, self.b), 15)  # Expected output: 15

# Run tests
if __name__ == '__main__':
    unittest.main()

"""
Guide:
1. Define a function to test (e.g., add(a, b)).
2. Create a TestCase class inheriting from unittest.TestCase.
3. Write methods with names starting with `test_` to define test cases.
   - Use `assertEqual` to check expected output.
   - Use `assertRaises` to check for exceptions.
4. Optionally, use `setUp` and `tearDown` methods to prepare/cleanup before/after tests.
5. Run tests by executing the file: python unit_test_guide.py
"""
