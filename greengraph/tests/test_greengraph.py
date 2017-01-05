from greengraph.greengraph import Greengraph
from geocoder import Geocoder
import unittest
import mock
import numpy as np

class TestGreengraph(unittest.TestCase):

    @mock.patch("geopy.geocoders.GoogleV3", side_effect = Geocoder)
    def test_geolocate(self, whatever):
        # Test some random location
        self.assertEqual(tuple(Greengraph("Start", "End").geolocate("Ljubljana")), (46.0569465, 14.5057515, 0.0))
        self.assertEqual(tuple(Greengraph("Start", "End").geolocate("Nordkapp")), (71.169493, 25.783164, 0.0))
        # Test some extreme location (north pole)
        self.assertEqual(tuple(Greengraph("Start", "End").geolocate("North")), (95, 0, 0.0))
        self.assertEqual(tuple(Greengraph("Start", "End").geolocate("South")), (-95, 0, 0.0))

    def test_location_sequence(self):
        # Test only one step
        for i in range(1):
            self.assertEqual(Greengraph("Start","End").location_sequence((0,0,0), (5,5,0), 1)[0][i],0)
        # Test the same starting and ending location_sequence
        for i in range(3):
            for j in range(2):
                self.assertEqual(Greengraph("Start","End").location_sequence((5,5,0), (5,5,0), 3)[i][j], 5)
