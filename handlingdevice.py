"""

Class definitions of the handling devices.

Built 2017 by Bastian Burger for blik and shared with Solopex.

"""

class HandlingDevice:
    """
    Abstract Definition of a load carrier with kartesian coordinates, dimensions, a maximum mooving speed and a boolean attribute if loaded or not.
    """
    def __init__(self, coordinates, dimensions, max_speed, loaded):
        self.coordinates = coordinates
        self.dimensions = dimensions
        self.max_speed = max_speed
        self.loaded = False

    def load(self):
        if self.loaded:
            print("Already loaded")
        else:
            self.loaded = True
        return

    def unload(self):
        if not self.loaded:
            print("Nothing to unload")
        else:
            self.loaded = False
        return

class Forklift(HandlingDevice):
    def __init__(self):
        HandlingDevice.__init__(self)
        # Estimated Dimensions
        self.dimensions = (1.20, 2.40, 2.40)
        self.max_speed = 8.00
