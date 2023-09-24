import sys
import unittest
sys.path.insert(0, '/home/team22/repos/supply-backend/src')
from models.FleetManager import FleetManager


class fleetManagerTests(unittest.TestCase):

    #Tests the getters implemented in FleetManager.py within 'models' folder
    def testFleetManagerGetters(self):
        # Create a new FleetManager instance
        testFM = FleetManager(1, "fleetManagerMike@gmail.com", "michaeljordan23", "Chicagobu11$", "Michael", "Jordan")
        
        # Test getId method
        self.assertEqual(testFM.getId(), 1)
        
        # Test getEmail method
        self.assertEqual(testFM.getEmail(), "fleetManagerMike@gmail.com")
        
        # Test getUsername method
        self.assertEqual(testFM.getUsername(), "michaeljordan23")
        
        # Test getPassword method
        self.assertEqual(testFM.getPassword(), "Chicagobu11$")
        
        # Test getFName method
        self.assertEqual(testFM.getFName(), "Michael")
        
        # Test getLName method
        self.assertEqual(testFM.getLName(), "Jordan")

    #Tests the setters implemented in FleetManager.py within 'models' folder
    def testFleetManagerSetters(self):
        # Create a new FleetManager instance
        testFM = FleetManager(1, "fleetManagerMike@gmail.com", "michaeljordan23", "Chicagobu11$", "Michael", "Jordan")
        
        # Test setId method
        testFM.setId(2)
        self.assertEqual(testFM.getId(), 2)
        
        # Test setEmail method
        testFM.setEmail("fleetManagerLarry@gmail.com")
        self.assertEqual(testFM.getEmail(), "fleetManagerLarry@gmail.com")
        
        # Test setUsername method
        testFM.setUsername("larrybird33")
        self.assertEqual(testFM.getUsername(), "larrybird33")
        
        # Test setPassword method
        testFM.setPassword("Bo$tonC3ltics")
        self.assertEqual(testFM.getPassword(), "Bo$tonC3ltics")
        
        # Test setFName method
        testFM.setFName("Larry")
        self.assertEqual(testFM.getFName(), "Larry")
        
        # Test setLName method
        testFM.setLName("Bird")
        self.assertEqual(testFM.getLName(), "Bird")
    
    
    def testStr(self):
        # Create a new FleetManager instance
        testFM = FleetManager(1, "fleetManagerMike@gmail.com", "michaeljordan23", "Chicagobu11$", "Michael", "Jordan")
        
        # Test __str__ method
        expected_output = "Fleet Manager ID: 1\nEmail: fleetManagerMike@gmail.com\nUsername: michaeljordan23\nPassword: Chicagobu11$\nFirst Name: Michael\nLast Name: Jordan"
        self.assertEqual(str(testFM), expected_output)


if __name__ == '__main__':
    unittest.main()