# Hold obvious parameters for the Triangle.
class Triangle():
    def __init__(self):
        # initialize all empty parameters
        self.triValues{
            "s1":0,
            "s2":0,
            "s3":0,
            "angles":[0,0,0], # a[0] = a1 etc
            "v1":None,
            "v2":None,
            "v3":None,
        }

    def checkLawOfSines(self):
        # Need to fill 

    def sumOfAllAngles(self):
        if self.triValues["angles"].count(0) == 2:
            self.triValues["angles"][self.triValues["angles"].index(0)] = 180 - sum(self.triValues["angles"])

    def checkIfRA(self): # Check If Right Angle 
        if 90 in self.angles:
            return True
        else:
            return False
        
    def setVertex(self, name, x, y):
        self.triValues[name] = (x,y)

    def setValue(self, name, value):
        if name in self.triValues:
            self.triValues[name] = value
        elif(name == "a1"):
            self.triValues["angles"][0] = value
        elif(name == "a2"):
            self.triValues["angles"][1] = value
        elif(name == "a3"):
            self.triValues["angles"][2] = value

    def checkValueExist(self, name):
        if name in self.triValues || name == "a1" || name == "a2" || name == "a2":
            return True
        else: 
            return False