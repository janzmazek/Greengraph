class Geocoder(object):
    def __init__(self,domain):
        self.domain = domain

    def geocode(self, place, exactly_one):
        #First without fixture files
        if place == "Ljubljana":
            return [[1,(46.0569465, 14.5057515,0.0)],[3,4]]
