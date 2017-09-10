"""

Class definitions of the load carriers.

Built 2017 by Bastian Burger for blik and shared with Solopex.

"""

class LoadCarrier:
    """
    Abstract Definition of a load carrier with kartesian coordinates and dimensions.
    """
    def __init__(self, coordinates, dimensions):
        self.coordinates = coordinates
        self.dimensions = dimensions

    def area(self):
        return self.dimensions[0] * self.dimensions[1]

    def volume(self):
        return self.area * self.dimensions[2]

class MeshBox(LoadCarrier):
    def __init__(self, coordinates):
        LoadCarrier.__init__(self, coordinates, (1.20, 0.80, 0.97))

class Pallet(LoadCarrier):
    def __init__(self):
        LoadCarrier.__init__(self)
        self.dimensions = (1.20, 0.80, 1.60)
