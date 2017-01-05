import yaml

class Geocoder(object):
    def __init__(self,domain):
        self.domain = domain

    def geocode(self, place, exactly_one):
        with open("fixtures/locations.yaml","r") as file:
            locations = yaml.load(file)
        return locations[place]
