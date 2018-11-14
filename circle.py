# Hold obvious parameters for the circle
import math
from sympy.geometry import Circle as c, Point 

class Circle():
    def __init__(self, *args):
        self.cirValues = {
            "r": 0,
            "c": None,
            "d": 0,
            "ar_cir": 0, 
            "circumference": 0,
        }
        self.geoC = None

    # Creating a Circle using the sympy module for the purposes of intersections and such 
    def makeGeoT(self):
        if self.cirValues["r"] and self.cirValues["c"] :
            self.GeoC = c(Point(self.cirValues["c"][0],self.cirValues["c"][1]), self.cirValues["r"] )

    # Get diameter from radius
    def getDfromR(self):
        if self.cirValues["r"] and not self.cirValues["d"]:
            self.cirValues["d"] = 2*self.cirValues["r"]
    
    # Get radius from diameter
    def getRfromD(self):
        if self.cirValues["d"] and not self.cirValues["r"]:
            self.cirValues["r"] = self.cirValues["d"]/2

    # Find the given area
    def findArea(self):
        if not self.cirValues["ar_cir"]:
            if self.cirValues["r"]:
                self.cirValues["ar_cir"] = pow(self.cirValues["r"],2) * math.pi 

    # Find the given circumference
    def findCircumference(self):
        if not self.cirValues["circumference"]:
            if self.cirValues["r"]:
                self.cirValues["circumference"] = 2*math.pi*self.cirValues["r"]
            
    def setCenter(self, x, y):
        self.cirValues["c"] = (x,y)

    def setValue(self, name, value):
        if name in self.cirValues:
            self.cirValues[name] = value

    def getValue(self, name):
        if name in self.cirValues:
            return self.cirValues[name] 

    def checkValueExist(self, name):
        if name in self.cirValues:
            return True
        else: 
            return False

    def solve(self):
        self.getDfromR()
        self.getRfromD()
        self.findArea()
        self.findCircumference()

        
    def printValues(self):
        print(self.cirValues)

