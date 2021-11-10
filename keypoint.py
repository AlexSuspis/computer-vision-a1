class Keypoint:

    #location as a (x,y) tuple
    def __init__(self, location):

        self.location = location
        self.orientation = None
        self.magnitude = None
        self.descriptor = None


    def getLocation(self):
        return self.location

    def setLocation(self, value):
        self.location = value

    def getOrientation(self):
        return self.orientation

    def setOrientation(self, value):
        self.orientation = value

    def getMagnitude(self):
        return self.magnitude

    def setMagnitude(self, value):
        self.magnitude = value

    def getDescriptor(self):
        return self.descriptor

    def setDescriptor(self, value):
        self.descriptor = value


