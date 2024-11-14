import unittest
from unittest.mock import patch

from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        # Set up a user instance for testing
        self.user = User(username="test_user", password="secure123", age=25)

    def test_initialization(self):
        # Check that the user is initialized correctly
        self.assertEqual(self.user.username, "test_user")
        self.assertEqual(self.user.password, "secure123")
        self.assertEqual(self.user.age, 25)
        self.assertFalse(self.user.loggedIn)  # User should not be logged in initially

    def test_login_successful(self):
        # Test successful login with correct password
        self.user.login("secure123")
        self.assertTrue(self.user.loggedIn)  # User should be logged in

    @patch("builtins.print")  # Mock the print function to capture output
    def test_login_incorrect_password(self, mock_print):
        # Test login with incorrect password
        self.user.login("wrong_password")
        
        # Check that an error message was printed
        mock_print.assert_called_with("Incorrect password")
        
        # Ensure the user is still logged out
        self.assertFalse(self.user.loggedIn)

       
    """
    @patch("builtins.print"): This decorator from unittest.mock replaces the print function with a mock object, allowing us to capture and verify printed output.
    mock_print.assert_called_with("Incorrect password"): Checks that the error message "Incorrect password" was printed when an incorrect password is provided.
    self.assertFalse(self.user.loggedIn): Confirms that the user remains logged out.
    """ 
    def test_logout(self):
        # Test that logout works correctly
        self.user.login("secure123")  # Log in the user first
        self.user.logout()
        self.assertFalse(self.user.loggedIn)  # User should be logged out

if __name__ == "__main__":
    unittest.main()