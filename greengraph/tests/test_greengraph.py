from greengraph.greengraph import Greengraph
import unittest
import mock

class TestGreengraph(unittest.TestCase):
    def geocode_side_effect(place, exacly_one):
        #First without fixture files
        if place == "Ljubljana":
            return [Location(Ljubljana, Slovenia, (46.0569465, 14.5057515, 0.0))]

    @mock.patch('geopy.geocoders.GoogleV3', side_effect = geocode_side_effect)
    def test_geolocate(self, place):
        # Make some greengraph object
        greengraph = Greengraph("London","Ljubljana")
        self.assertEqual(Greengraph().geolocate("Ljubljana"), (46.0569465, 14.5057515, 0.0))
