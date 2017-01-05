class Requester(object):
    # This is a mock class (works offline instead of requests.get)
    def __init__(self, base, params):
        self.base = base
        self.params = params
        # Use parameter "zoom" to specify fixture file
        if params["zoom"] == "blue":
            with open("fixtures/blue.png", "rb") as imageFile:
                self.content = imageFile.read()
        elif params["zoom"] == "yellow":
            with open("fixtures/yellow.png", "rb") as imageFile:
                self.content = imageFile.read()
        elif params["zoom"] == "green":
            with open("fixtures/green.png", "rb") as imageFile:
                self.content = imageFile.read()
        elif params["zoom"] == "plague":
            with open("fixtures/plague.png", "rb") as imageFile:
                self.content = imageFile.read()
