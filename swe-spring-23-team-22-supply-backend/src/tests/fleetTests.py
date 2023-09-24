import sys
import unittest
sys.path.insert(0, '/home/team22/repos/supply-backend/src')
from models.Fleet import Fleet



class fleetTests(unittest.TestCase):

    #Tests the getters implemented in Fleet.py within 'models' folder
    def testFleetGetters(self):
    	#Initialize New Fleet Instance
        #Fleet instance with ID: 1, Fleet Name: 'A', Plugin Type: 'vaccines', and a restock location at St. Edward's
        testFleet = Fleet(1, 'A', 'vaccines', [ "-97.7579406", "30.231722" ])

        # Test getId method
        self.assertEqual(testFleet.getId(), 1)

        # Test getFleetName method
        self.assertEqual(testFleet.getFleetName(), 'A')

        # Test getPluginType method
        self.assertEqual(testFleet.getPluginType(), 'vaccines')

        # Test getRestockLocation method
        self.assertEqual(testFleet.getRestockLocation(), [ "-97.7579406", "30.231722" ])

    #Tests the setters implemented in Fleet.py within 'models' folder
    def testFleetSetters(self):
        testFleet = Fleet(2, 'A', 'vaccines', [ "-97.7579406", "30.231722" ])

        # Test setId method
        testFleet.setId(3)
        self.assertEqual(testFleet.getId(), 3)

        # Test setFleetName method
        testFleet.setFleetName('C')
        self.assertEqual(testFleet.getFleetName(), 'C')

        # Test setPluginType method
        testFleet.setPluginType('blood')
        self.assertEqual(testFleet.getPluginType(), 'blood')

        # Test setRestockLocation method
        testFleet.setRestockLocation(["-97.7404","30.2747"])
        self.assertEqual(testFleet.getRestockLocation(), ["-97.7404","30.2747"])


    def testFleetToString(self):
        testFleet = Fleet(3, 'A', 'vaccines', [ "-97.7579406", "30.231722" ])
        expected_output = "Fleet ID: 3\nFleet Name: A\nPlugin Type: vaccines\nRestock Location: -97.7579406, 30.231722"
        self.assertEqual(str(testFleet), expected_output)

if __name__ == '__main__':
    unittest.main()