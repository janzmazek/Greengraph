from greengraph.map import Map
import unittest
import mock
from requester import Requester

class testMap(unittest.TestCase):

    @mock.patch("requests.get", side_effect = Requester)
    def test_green(self,whatever):
        print(Map(10, 10, size=(400,400)).green(1.1))
