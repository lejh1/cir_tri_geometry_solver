# Hold obvious parameters for the circle
import math

class Circle():
    def __init__(self, *args):
        self.cirValues = {
            "r": 0,
            "c": None,
            "d": 0,
            "area": 0, 
            "circumference": 0,
        }

    def getRfromD(self):
        if self.cirValues["r"] and not self.cirValues["d"]:
            self.cirValues["d"] = 2*self.cirValues["r"]
    
    def getDfromR(self):
        if self.cirValues["d"] and not self.cirValues["r"]:
            self.cirValues["r"] = self.cirValues["d"]/2

    def findArea(self):
        if not self.area:
            if self.cirValues["r"]:
                self.area = pow(self.cirValues["r"],2) * math.pi 

    def findCircumference(self):
        if not self.cirValues["circumference"]:
            if self.cirValues["r"]:
                self.cirValues["circumference"] = 2*math.pi*self.cirValues["r"]
            
    def setCenter(self, x, y):
        self.cirValues["c"] = (x,y)

    def setValue(self, name, value):
        if name in self.cirValues:
            self.cirValues[name] = value

    def checkValueExist(self, name):
        if name in self.cirValues:
            return True
        else: 
            return False
        
    def printValues(self):
        print(self.cirValues)

