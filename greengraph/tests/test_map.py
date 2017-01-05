from greengraph.map import Map
import unittest
import mock
from requester import Requester

class testMap(unittest.TestCase):

    @mock.patch("requests.get", side_effect = Requester)
    def test_green(self,whatever):
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

    def test_count_green(self):
        self.assertEqual((Map(10,10, satellite=True, zoom="green", size=(400,400)).count_green(0)),103097) #Limit case (all greens)
        self.assertEqual((Map(10,10, satellite=True, zoom="green", size=(400,400)).count_green(1)), 10369)
        self.assertEqual((Map(10,10, satellite=True, zoom="green", size=(400,400)).count_green(2)),0) #Limit case (no greens)


    def test_show_green(self):
        pass
