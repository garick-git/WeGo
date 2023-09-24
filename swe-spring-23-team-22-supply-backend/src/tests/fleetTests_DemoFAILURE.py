import sys
import unittest
sys.path.insert(0, '/home/team22/repos/supply-backend/src')
from models.Fleet import Fleet



class fleetTests_DemoFAILURE(unittest.TestCase):

    # This test is intentially meant to fail in order to demonstrate what it looks like when a test case is failed.
    # We should expect to see in the console output is this test failing and the 2 tests below it succeeding 
    def testFleetGetters_FAILURE(self):
    	#Initialize New Fleet Instance
        #Fleet instance with ID: 1, Fleet Name: 'A', Plugin Type: 'vaccines', and a restock location at St. Edward's
        testFleet = Fleet(1, 'A', 'vaccines', [ "-97.7579406", "30.231722" ])

        # Test getId method
        self.assertEqual(testFleet.getId(), 999)

        # Test getFleetName method
        self.assertEqual(testFleet.getFleetName(), 'C')

        # Test getPluginType method
        self.assertEqual(testFleet.getPluginType(), 'vaccines')

        # Test getRestockLocation method
        self.assertEqual(testFleet.getRestockLocation(), [ "-97.7579406", "30.231722" ])


if __name__ == '__main__':
    unittest.main()