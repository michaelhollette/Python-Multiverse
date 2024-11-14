import unittest
from scooter import Scooter
from user import User

class TestScooter(unittest.TestCase):
    def setUp(self):
        self.scooter = Scooter("Liverpool Street")
        self.user = User("David" ,"password123", 20)

    def test_initialization(self):
        # Check that a new scooter is docked, fully charged, and not broken
        self.assertEqual(self.scooter.station, "Liverpool Street")
        self.assertIsNone(self.scooter.user)
        self.assertEqual(self.scooter.charge, 100)
        self.assertFalse(self.scooter.isBroken)
    
    def serial_assignment(self):
        # Check that each scooter has a unique serial number
        self.scooter1 = Scooter("Station A")
        self.scooter2 = Scooter("Station B")
        self.assertNotEqual(self.scooter1.serial,self.scooter2.serial)

    def test_rent_scooter_successful(self):
        # Ensure scooter can be rented if it has sufficient charge and is not broken

        self.scooter.charge = 80
        self.scooter.rent(self.user)
        self.assertIsNone(self.scooter.station)
        self.assertEqual(self.scooter.user, self.user)
    def test_rent_scooter_needs_charge(self):
        # Ensure scooter cannot be rented if the charge is below 20%
        self.scooter.charge = 10
        with self.assertRaises(Exception) as context:
            self.scooter.rent(self.user)
        self.assertEqual(str(context.exception), "Scooter needs to charge")

    def test_rent_scooter_needs_repair(self):
        # Ensure scooter cannot be rented if it's broken, even with sufficient charge
        self.scooter.charge = 80
        self.scooter.isBroken = True
        with self.assertRaises(Exception) as context:
            self.scooter.rent(self.user)
        self.assertEqual(str(context.exception), "Scooter needs repair")

    def test_dock_scooter(self):
        # Test docking a scooter at a station and clearing the user
        self.scooter.charge = 80
        self.scooter.rent(self.user)  # Rent out the scooter
        self.scooter.dock("North Station")
        self.assertEqual(self.scooter.station, "North Station")
        self.assertIsNone(self.scooter.user)

    def test_dock_scooter_resets_station(self):
        # Ensure docking updates station and clears user information
        self.scooter.rent(self.user)
        self.scooter.dock("South Station")
        self.assertEqual(self.scooter.station, "South Station")
        self.assertIsNone(self.scooter.user)

if __name__ == "__main__":
    unittest.main()