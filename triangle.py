# Hold obvious parameters for the Triangle.
# Not using the sympy Triangle class because it has limitations so decided to build my own class 
from calcs import *
from sympy.geometry import Triangle as t, Point 
class Triangle():
    def __init__(self):
        # initialize all empty parameters
        # Parameters stored in a dict for easy access search (Yay O(1) search time!)
        self.triValues = {
            "s1":0,
            "s2":0,
            "s3":0,
            "angles":[0,0,0], # a[0] = "a1" etc
            "v1":None,
            "v2":None,
            "v3":None,
            "ar_tri": 0,
            "per_tri":0
        }
        self.GeoT = None
 
    # Creating a Triangle using the sympy module for the purposes of intersections and such 
    def makeGeoT(self):
        if not len(self.getMissingVertices()):
            self.GeoT = t((self.triValues["v1"][0],self.triValues["v1"][1]),(self.triValues["v2"][0],self.triValues["v2"][1]),(self.triValues["v3"][0],self.triValues["v3"][1]))
        elif self.countSides() == 3:
            self.GeoT = t(sss=(self.triValues["s1"],self.triValues["s2"],self.triValues["s3"]))

    # If two angles are known, fill in the last one 
    def sumOfAllAngles(self):
        if self.triValues["angles"].count(0) == 1:
            self.triValues["angles"][self.triValues["angles"].index(0)] = 180 - sum(self.triValues["angles"])
            return True
        else:
            return False

    # Check If Right Angle 
    def checkIfRA(self): 
        if 90 in self.angles:
            return True
        else:
            return False

    # Sets the vertex of the given name of a Triangle parameter
    def setVertex(self, name, x, y):
        self.triValues[name] = (x,y)

    # Sets the value of the given name of a Triangle parameter
    def setValue(self, name, value):
        if name in self.triValues:
            self.triValues[name] = value
        elif(name == "a1"):
            self.triValues["angles"][0] = value
        elif(name == "a2"):
            self.triValues["angles"][1] = value
        elif(name == "a3"):
            self.triValues["angles"][2] = value
    
    # Returns the value of the given name of a Triangle parameter
    def getValue(self, name):
        if name in self.triValues:
            return self.triValues[name]
        elif(name == "a1"):
            return self.triValues["angles"][0] 
        elif(name == "a2"):
            return self.triValues["angles"][1] 
        elif(name == "a3"):
            return self.triValues["angles"][2] 

    # Checks if the name given exists as a parameter of the Triangle Class
    def checkValueExist(self, name):
        if name in self.triValues or name == "a1" or name == "a2" or name == "a2":
            return True
        else: 
            return False
    
    def findPerimeter(self):
        if not self.triValues["per_tri"]:
            if self.triValues["s1"] and self.triValues["s2"] and self.triValues["s3"]:
                self.triValues["per_tri"] = self.triValues["s1"] + self.triValues["s2"] + self.triValues["s3"]
            
    def findArea(self):
        if not self.triValues["ar_tri"]:
            if self.triValues["s1"] and self.triValues["s2"] and self.triValues["s3"]:
                self.triValues["ar_tri"] = heronsFormula(self.triValues["s1"],self.triValues["s2"],self.triValues["s3"])

    # Prints all triangle values as a dict
    def printValues(self):
        print(self.triValues)

    # Returns a list of the sides that are missing 
    def getMissingSides(self):
        missing = list()
        for i in range(1,4):
            if self.triValues["s"+str(i)] == None:
                missing.append("s"+str(i))
        return missing

    # Returns a list of the angles that are missing 
    def getMissingAngles(self): 
        missing = list()
        for i in range(3):
            if self.triValues["angles"][i] == None:
                missing.append("a"+str(i+1))
        return missing

    # Returns a list of the angles that are missing 
    def getMissingVertices(self): 
        missing = list()
        for i in range(1,4):
            if self.triValues["v"+str(i)] == None:
                missing.append("v"+str(i))
        return missing


    # Returns number of found sides
    def countSides(self):
        count = 0
        for i in range(1,4):
            if self.triValues["s"+str(i)] != 0:
                count+=1
        return count

    # Returns number of found angles
    def countAngles(self): 
        count = 0
        if self.triValues["angles"][0] != 0:
            count+=1
        if self.triValues["angles"][1] != 0:
            count+=1
        if self.triValues["angles"][2] != 0:
            count+=1
        return count

    def solveSidesWVertices(self):
        if self.triValues["v1"] and self.triValues["v2"]:
            self.triValues["s3"] = distanceFormula(self.triValues["v1"][0],self.triValues["v1"][1],self.triValues["v2"][0],self.triValues["v2"][1])
        if self.triValues["v3"] and self.triValues["v2"]:
            self.triValues["s1"] = distanceFormula(self.triValues["v2"][0],self.triValues["v2"][1],self.triValues["v3"][0],self.triValues["v3"][1])
        if self.triValues["v1"] and self.triValues["v3"]:
            self.triValues["s2"] = distanceFormula(self.triValues["v1"][0],self.triValues["v1"][1],self.triValues["v3"][0],self.triValues["v3"][1])

    def solve(self):
        self.solveSidesWVertices() # Solve for any missing sides from vertices 
        # 2 side 1 angle
        if self.countSides()==2 and self.countAngles()==1:
            # SAS
            if not self.triValues["s1"] and self.triValues["angles"][0] and self.triValues["s2"] and self.triValues["s3"]: # Abc
                self.triValues["s1"] = lawOfCosinesSAS(self.triValues["angles"][0],self.triValues["s2"],self.triValues["s3"])
            elif not self.triValues["s2"] and self.triValues["angles"][1] and self.triValues["s1"] and self.triValues["s3"]: # Bac
                self.triValues["s2"] = lawOfCosinesSAS(self.triValues["angles"][1],self.triValues["s3"],self.triValues["s1"])
            elif not self.triValues["s3"] and self.triValues["angles"][2] and self.triValues["s2"] and self.triValues["s1"]: # Cab
                self.triValues["s3"] = lawOfCosinesSAS(self.triValues["angles"][2],self.triValues["s1"],self.triValues["s2"])
            # SSA
            elif not self.triValues["angles"][1] and self.triValues["s1"] and self.triValues["s2"] and self.triValues["angles"][0]: # abA 
                self.triValues["angles"][1] = lawOfSinesSSA(self.triValues["s1"],self.triValues["s2"],self.triValues["angles"][0]) 
            elif not self.triValues["angles"][2] and self.triValues["s1"] and self.triValues["s3"] and self.triValues["angles"][0]: # acA 
                self.triValues["angles"][2] = lawOfSinesSSA(self.triValues["s1"], self.triValues["s3"],  self.triValues["angles"][0])
            elif not self.triValues["angles"][1] and self.triValues["s3"] and self.triValues["s2"] and self.triValues["angles"][2]: # cbC
                self.triValues["angles"][1] =  lawOfSinesSSA(self.triValues["s3"], self.triValues["s2"],  self.triValues["angles"][2])
            elif not self.triValues["angles"][0] and self.triValues["s3"] and self.triValues["s1"] and self.triValues["angles"][2]: # caC
                self.triValues["angles"][0] =  lawOfSinesSSA(self.triValues["s3"], self.triValues["s1"],  self.triValues["angles"][2])
            elif not self.triValues["angles"][2] and self.triValues["s2"] and self.triValues["s3"] and self.triValues["angles"][1]: # bcB
                self.triValues["angles"][2] =  lawOfSinesSSA(self.triValues["s2"], self.triValues["s3"],  self.triValues["angles"][1])
            elif not self.triValues["angles"][0] and self.triValues["s2"] and self.triValues["s1"] and self.triValues["angles"][1]: # baB
                self.triValues["angles"][0] =  lawOfSinesSSA(self.triValues["s2"], self.triValues["s1"],  self.triValues["angles"][1])
        # 1 side 2 angles 
        # 2 sides 2 angle
        # both lead to next if statement 
        if self.sumOfAllAngles(): # if all angles exist 
            if self.countSides() == 1: # 1 side 
                if not self.triValues["s1"] and self.triValues["s2"]: # AbB
                    self.triValues["s1"] = lawOfSinesAAS(self.triValues["angles"][0],self.triValues["s2"],self.triValues["angles"][1])
                elif not self.triValues["s1"] and self.triValues["s3"]: # AcC
                    self.triValues["s1"] = lawOfSinesAAS(self.triValues["angles"][0],self.triValues["s3"],self.triValues["angles"][2])
                elif not self.triValues["s2"] and self.triValues["s3"]: # BcC
                    self.triValues["s2"] = lawOfSinesAAS(self.triValues["angles"][1],self.triValues["s3"],self.triValues["angles"][2])
                elif not self.triValues["s2"] and self.triValues["s1"]: # BaA
                    self.triValues["s2"] = lawOfSinesAAS(self.triValues["angles"][1],self.triValues["s1"],self.triValues["angles"][0])
                elif not self.triValues["s3"] and self.triValues["s1"]: # CaA
                    self.triValues["s3"] = lawOfSinesAAS(self.triValues["angles"][2],self.triValues["s1"],self.triValues["angles"][0])
                elif not self.triValues["s3"] and self.triValues["s2"]: # CbB
                    self.triValues["s3"] = lawOfSinesAAS(self.triValues["angles"][2],self.triValues["s2"],self.triValues["angles"][1])
            if self.countSides() == 2: # 2 sides; this is an if not an elif so that we can continue to solve for 2 sides after solving for 1
                if not self.triValues["s1"] and self.triValues["s2"]: # AbB
                    self.triValues["s1"] = lawOfSinesAAS(self.triValues["angles"][0],self.triValues["s2"],self.triValues["angles"][1])
                elif not self.triValues["s1"] and self.triValues["s3"]: # AcC
                    self.triValues["s1"] = lawOfSinesAAS(self.triValues["angles"][0],self.triValues["s3"],self.triValues["angles"][2])
                elif not self.triValues["s2"] and self.triValues["s3"]: # BcC
                    self.triValues["s2"] = lawOfSinesAAS(self.triValues["angles"][1],self.triValues["s3"],self.triValues["angles"][2])
                elif not self.triValues["s2"] and self.triValues["s1"]: # BaA
                    self.triValues["s2"] = lawOfSinesAAS(self.triValues["angles"][1],self.triValues["s1"],self.triValues["angles"][0])
                elif not self.triValues["s3"] and self.triValues["s1"]: # CaA
                    self.triValues["s3"] = lawOfSinesAAS(self.triValues["angles"][2],self.triValues["s1"],self.triValues["angles"][0])
                elif not self.triValues["s3"] and self.triValues["s2"]: # CbB
                    self.triValues["s3"] = lawOfSinesAAS(self.triValues["angles"][2],self.triValues["s2"],self.triValues["angles"][1])
        # if all sides exist 
        elif self.countSides()==3: 
            if not self.triValues["angles"][0]:
                self.triValues["angles"][0] = lawOfCosinesSSS(self.triValues["s1"],self.triValues["s2"],self.triValues["s3"])
            if not self.triValues["angles"][1]:
                self.triValues["angles"][1] = lawOfCosinesSSS(self.triValues["s2"],self.triValues["s3"],self.triValues["s1"])
            if not self.triValues["angles"][2]:
                self.triValues["angles"][2] = lawOfCosinesSSS(self.triValues["s3"],self.triValues["s1"],self.triValues["s2"])
        if len(self.getMissingVertices()):
            print("Need to solve for vertices using the known sides and angles ***********")
        self.findPerimeter()
        self.findArea()
        self.makeGeoT()

