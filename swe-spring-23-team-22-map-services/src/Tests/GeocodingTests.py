import unittest

from src.BackEndGeocoding.GeocodingUtils import adressToGeocode, getRouteFromGeocodes


class TestMapbox(unittest.TestCase):

    def test_adressToGeocode(self):
        # Test case 1: Valid address input
        self.assertEqual(adressToGeocode("1647 Post Road, San Marcos, TX"), [-97.9407, 29.8696])

        # Test case 2: Invalid address input
        self.assertEqual(adressToGeocode("INVALID ADDRESS"), None)

    def test_getRouteFromGeocodes(self):
        # Test case 1: Valid geocodes input
        self.assertEqual(getRouteFromGeocodes([-97.9407, 29.8696], [-97.9413, 29.8765]), [[-97.94067, 29.86955], [-97.94022, 29.87252], [-97.9401, 29.87416], [-97.94003, 29.87564], [-97.94049, 29.876], [-97.94106, 29.87645], [-97.94126, 29.87648], [-97.94146, 29.8765]])

        # Test case 2: Invalid geocodes input
        self.assertEqual(getRouteFromGeocodes([0, 0], [0, 0]), None)


if __name__ == '__main__':
    unittest.main()