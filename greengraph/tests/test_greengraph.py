from greengraph.greengraph import Greengraph
from geocoder import Geocoder
import unittest
import mock
import numpy as np

class TestGreengraph(unittest.TestCase):

    @mock.patch("geopy.geocoders.GoogleV3", side_effect = Geocoder)
    def test_geolocate(self, whatever):
        self.assertEqual(Greengraph("Start", "End").geolocate("Ljubljana"), (46.0569465, 14.5057515, 0.0))

    def test_location_sequence(self):
        # Equal position (Ljubljana)
        self.assertEqual(Greengraph("Start","End").location_sequence((46.0569465, 14.5057515, 0.0), (46.0569465, 14.5057515, 0.0), 3),
        np.array([[46.0569465, 14.5057515],[46.0569465, 14.5057515],[46.0569465, 14.5057515]])).all()
