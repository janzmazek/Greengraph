from greengraph.greengraph import Greengraph
from geocoder import Geocoder
import unittest
import mock

class TestGreengraph(unittest.TestCase):

    @mock.patch("geopy.geocoders.GoogleV3", side_effect = Geocoder)
    def test_geolocate(self, place):
        self.assertEqual(Greengraph("London","Ljubljana").geolocate("Ljubljana"), (46.0569465, 14.5057515, 0.0))
