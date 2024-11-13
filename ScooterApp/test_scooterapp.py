import unittest
from unittest.mock import patch
import io

from scooter import Scooter
from user import User
from scooterapp import ScooterApp

class TestScooterApp(unittest.TestCase):
    def setUp(self):
        self.app = ScooterApp()
        self.app.stations={
            "Central Station": [],
            "North Station": [],
            "East Station": []
        }

    def test_register_user_successful(self):
        # Register a user successfully
        user = self.app.registerUser("test_user", "password123", 25)
        self.assertIn("test_user", self.app.registeredUsers)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")

    @patch('builtins.print')
    def test_register_user_already_registered(self, mock_print):
        # Test registering a user who is already registered
        self.app.registerUser("test_user", "password123", 25)
        self.app.registerUser("test_user", "password123", 25)
        mock_print.assert_called_with("test_user has already been registered")

    @patch('builtins.print')
    def test_register_user_too_young(self, mock_print):
        # Test registering a user who is under 18
        self.app.registerUser("young_user", "password123", 17)
        mock_print.assert_called_with('young_user is too young to register')

    def test_login_user_successful(self):
        # Successfully log in a registered user
        self.app.registerUser("test_user", "password123", 25)
        self.app.loginUser("test_user", "password123")
        self.assertTrue(self.app.registeredUsers["test_user"].loggedIn)

    @patch("builtins.print")  
    def test_login_user_incorrect_password(self, mock_print):
        # Test login with incorrect password
        self.app.registerUser("test_user", "password123", 25)
        self.app.loginUser("test_user", "wrongpassword")
        mock_print.assert_called_with("Username or password is incorrect")

    @patch("builtins.print")  
    def test_login_user_not_registered(self, mock_print):
        # Test logging in a user who is not registered
        self.app.loginUser("unregistered_user", "password123")
        mock_print.assert_called_with("Username or password is incorrect")

    def test_logout_user_successful(self):
        # Successfully log out a registered user
        self.app.registerUser("test_user", "password123", 25)
        self.app.loginUser("test_user", "password123")
        self.app.logoutUser("test_user")
        self.assertFalse(self.app.registeredUsers["test_user"].loggedIn)

    @patch("builtins.print")
    def test_logout_user_not_logged_in(self,mock_print):
        # Test logging out a user who is not logged in
        self.app.registerUser("test_user", "password123", 25)
        self.app.logoutUser("test_user")
        mock_print.assert_called_with("test_user is not logged in")

    def test_create_scooter_successful(self):
        # Create a scooter and add it to a station
        scooter = self.app.createScooter("Central Station")
        self.assertIn(scooter, self.app.stations["Central Station"])

    @patch("builtins.print")  
    def test_create_scooter_invalid_station(self, mock_print):
        # Call createScooter with an invalid station
        self.app.createScooter("Unknown Station")
        
        # Check that print was called with the correct error message
        mock_print.assert_called_with("Unknown Station does not exist")    

    def test_dock_scooter_successful(self):
        # Dock a scooter at a station
        scooter = Scooter(station="Central Station")
        self.app.dockScooter(scooter, "Central Station")
        self.assertIn(scooter, self.app.stations["Central Station"])

    @patch("builtins.print")  # Mock the print function
    def test_dock_scooter_invalid_station(self, mock_print):
        # Attempt to dock a scooter at a non-existent station
        scooter = Scooter(station="Central Station")
        self.app.dockScooter(scooter, "Unknown Station")
        mock_print.assert_called_with("Station 'Unknown Station' does not exist")
    
    @patch("builtins.print")  # Mock the print function
    def test_dock_scooter_already_at_station(self, mock_print):
        # Attempt to dock a scooter that is already at the station
        scooter = Scooter(station="Central Station")
        self.app.dockScooter(scooter, "Central Station")
        
        self.app.dockScooter(scooter, "Central Station")
        mock_print.assert_called_with("Scooter is already at station Central Station")    


    def test_rent_scooter_successful(self):
        # Rent a scooter to a user
        scooter = self.app.createScooter("Central Station")
        user = self.app.registerUser("test_user", "password123", 25)
        self.app.rentScooter(scooter, user)
        self.assertNotIn(scooter, self.app.stations["Central Station"])
        self.assertEqual(scooter.user, user)


    @patch('builtins.print')
    def test_rent_scooter_already_rented(self, mock_print):
        # Attempt to rent a scooter that is already rented
        scooter = self.app.createScooter("Central Station")
        user1 = self.app.registerUser("user1", "password123", 25)
        user2 = self.app.registerUser("user2", "password123", 25)

        self.app.rentScooter(scooter, user1)
        self.app.rentScooter(scooter, user2)
        mock_print.assert_called_with('Scooter is already rented')


    @patch('sys.stdout', new_callable=io.StringIO)

    def test_print(self, mock_stdout):
        # Test the print method to see output of registered users and stations
        self.app.registerUser("user1", "password123", 25)
        self.app.registerUser("user2", "password123", 30)
        self.app.createScooter("Central Station")
        self.app.createScooter("North Station")

        self.app.print()
        

        output = mock_stdout.getvalue()

        self.assertIn("Registered users are:", output)
        self.assertIn("user1", output)
        self.assertIn("user2", output)
        self.assertIn("At Central Station, there are 1 scooters", output)
        self.assertIn("At North Station, there are 1 scooters", output)

if __name__ == "__main__":
    unittest.main()