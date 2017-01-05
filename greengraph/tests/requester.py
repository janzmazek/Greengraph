class Requester(object):
    def __init__(self, base, params):
        self.base = base
        self.params = params
        with open("fixtures/blue.png", "rb") as imageFile:
            self.content = imageFile.read()
