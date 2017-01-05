from greengraph.map import Map
import unittest
import mock
from requester import Requester

class testMap(unittest.TestCase):

    @mock.patch("requests.get", Requester)
    def test_green(self):
        # Test 10x10 color PNGs
        for i in range(10):
            for j in range(10):
                # Test green picture for some tresholds
                self.assertEqual(Map(10,10, satellite=True, zoom="green", size=(400,400)).green(0)[i][j],True) # Try limit value
                self.assertEqual(Map(10,10, satellite=True, zoom="green", size=(400,400)).green(1)[i][j],True)
                self.assertEqual(Map(10,10, satellite=True, zoom="green", size=(400,400)).green(2)[i][j],True)
                # Test yellow picture for some tresholds
                self.assertEqual(Map(10,10, satellite=True, zoom="yellow", size=(400,400)).green(1)[i][j],True)
                self.assertEqual(Map(10,10, satellite=True, zoom="yellow", size=(400,400)).green(2)[i][j],False)
                # Test blue picture for some tresholds
                self.assertEqual(Map(10,10, satellite=True, zoom="blue", size=(400,400)).green(0.5)[i][j],True)
                self.assertEqual(Map(10,10, satellite=True, zoom="blue", size=(400,400)).green(1)[i][j],False)
        for i in range(20):
            for j in range(20):
                # Test black-white plague doctor (only 20x20 because tests are slow)
                self.assertEqual(Map(10,10, satellite=True, zoom="plague", size=(400,400)).green(0)[i][j],True)
                self.assertEqual(Map(10,10, satellite=True, zoom="plague", size=(400,400)).green(1.1)[i][j],False)

    @mock.patch("requests.get", Requester)
    def test_count_green(self):
        self.assertEqual(Map(10,10, satellite=True, zoom="green", size=(400,400)).count_green(2),100)
        self.assertEqual(Map(10,10, satellite=True, zoom="blue", size=(400,400)).count_green(1),0)
        self.assertEqual(Map(10,10, satellite=True, zoom="yellow", size=(400,400)).count_green(1),100)
        self.assertEqual(Map(10,10, satellite=True, zoom="blue", size=(400,400)).count_green(0.5),100)
