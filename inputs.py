# Hold all possible input values 
# Uses Triangle and Circle objects
from sympy.geometry import intersection, Polygon, Segment
from triangle import Triangle
from circle import Circle
from calcs import *
class Inputs():
    def __init__(self, *args):
        self.inputs = { # dictionary of inputs for faster search and set
        "arc1":0,
        "arc2":0,
        "arc3":0,
        "ip1":None,
        "ip2":None,
        "ip3":None,
        "ar1":0,
        "ar2":0,
        "ar3":0,
        "sector1":0,
        "sector2":0,
        "sector3":0
        }
        self.numOfIPs = 0 # number of intersection points chosen by the user 
        self.Triangle = Triangle()
        self.Circle = Circle()
    
    # Sets values that isnt a tuple
    def set_value(self, name, value): # check if name is valid and if it is then replace it 
        if name in self.inputs:
            self.inputs[name] = value
        elif self.Triangle.checkValueExist(name):
            self.Triangle.setValue(name, value)
        elif self.Circle.checkValueExist(name):
            self.Circle.setValue(name, value)
        else:
            print("That parameter does not exist. Choose a new one.\n")
    
    # Sets vertex
    def set_vertex(self, name, x, y):
        if self.Triangle.checkValueExist(name):
            self.Triangle.setVertex(name, x, y)
        else:
            print("That parameter does not exist. Choose a new one.\n")
    # Sets Center
    def set_center(self, x , y): 
            self.Circle.setCenter(x, y)

    # Sets Intersection Points
    def set_intersection_points(self, name, x, y):
        if name in self.inputs:
            self.inputs[name] = (x,y)
        else:
            print("That parameter does not exist. Choose a new one.\n")

    # Prints all Values
    def printValues(self):
        print(self.inputs)
        self.Triangle.printValues()
        self.Circle.printValues()

    # Prints all Solvable Values
    def printSolvableValues(self):
        print(self.get_all())

    # Print prompt
    def printPrompt(self):
        print("Solvable Parameters (if null then it is non-solvable):")
        self.printSolvableValues()
        print("Non-Solvable Parameters:")
        ns = self.getNotSolvable()
        if len(ns) == 0:
            print("All Parameters were solved!!!")
        else:
            print(ns)

    # gets the value from a parameter name
    def get_value(self, name):
        if name in self.inputs:
            return self.inputs[name] 
        elif self.Triangle.checkValueExist(name):
            return self.Triangle.getValue(name)
        elif self.Circle.checkValueExist(name):
            return self.Circle.getValue(name)
        else:
            print("That parameter does not exist. Choose a new one.\n")
    
    # returns a dict with all the parameters
    def get_all(self):
        new_dict = self.inputs
        new_dict.update(self.Triangle.triValues)
        new_dict.update(self.Circle.cirValues)
        for i in new_dict:
            if not new_dict[i]:
                new_dict[i] = "null"
        return new_dict

    # Returns a list of all the not solvable parameters
    def getNotSolvable(self):
        notS = list()
        d = self.inputs
        d.update(self.Triangle.triValues)
        d.update(self.Circle.cirValues)
        for key, value in d.items():
            if value == "null":
                notS.append(key)
        if self.numOfIPs == 1:
            notS.remove("ip2")
            notS.remove("ip3")
            notS.remove("arc1")
            notS.remove("arc2")
            notS.remove("arc3")
            notS.remove("ar1")
            notS.remove("ar2")
            notS.remove("ar3")
            notS.remove("sector1")
            notS.remove("sector2")
            notS.remove("sector3")
        elif self.numOfIPs == 2:
            notS.remove("ip3")
            notS.remove("arc3")
            notS.remove("ar3")
            notS.remove("sector3")
        if "GeoT" in notS:
            notS.remove("GeoT")
        if "GeoC" in notS:
            notS.remove("GeoC")
        return notS

    # returns a count of the number of Intersection points
    def getIPs(self):
        count = 0
        for i in range(1,4):
            s = "ip" + str(i)
            if self.inputs[s]:
                count += 1
        return count

    # Returns a list with all the intersection points
    def getMissingIPs(self):
        missing = list()
        for i in range(1,4):
            s = "ip" + str(i)
            if not self.inputs[s]:
                missing.append(s)
        return missing

    # Function to solve when only 1 intersection point is chosen
    def oneIps(self):
        # get radius from center and ip1
        if not self.get_value("r") and self.get_value("c") and self.get_value("ip1"):
            c = self.get_value("c")
            ip = self.get_value("ip1")
            r = distanceFormula(c[0],c[1],ip[0],ip[1])
            self.set_value("r",r) 
        # Gets ip from center and radius 
        if not self.get_value("ip1") and self.Circle.GeoC and self.Triangle.GeoT:
            point = intersection(self.Circle.GeoC, self.Triangle.GeoT)
            self.set_intersection_points("ip1", float(point[0]), float(point[1]))
        self.Circle.solve()
    
    # Function to solve when only 2 intersection points is chosen
    def twoIps(self):
        # need to get center from two ips and radius?
        # get radius from center and ip1
        if not self.get_value("r") and self.get_value("c") and self.get_value("ip1"):
            c = self.get_value("c")
            ip = self.get_value("ip1")
            r = distanceFormula(c[0],c[1],ip[0],ip[1])
            self.set_value("r",r) 
        self.Circle.solve()
        # get radius from center and ip2
        if not self.get_value("r") and self.get_value("c") and self.get_value("ip2"):
            c = self.get_value("c")
            ip = self.get_value("ip2")
            r = distanceFormula(c[0],c[1],ip[0],ip[1])
            self.set_value("r",r) 
        self.Circle.solve()
        # Get Intersection points from input sympy geometry library when center and radius is known 
        if self.getIPs() != 2 and self.Triangle.GeoT and self.Circle.GeoC:  
            points = intersection(self.Circle.GeoC, self.Triangle.GeoT)
            if len(points) == 2:
                self.set_intersection_points("ip1",float(points[0][0]),float(points[0][1]))
                self.set_intersection_points("ip2",float(points[1][0]),float(points[1][1]))
        if self.getIPs() == 2 and self.get_value("r") and self.get_value("circumference"):
            c = self.get_value("ip1")
            ip = self.get_value("ip2")
            s = distanceFormula(c[0],c[1],ip[0],ip[1])
            angle = lawOfCosinesSSS(s, self.get_value("r"),self.get_value("r"))
            self.inputs["arc1"] = arcLength(self.get_value("r"), angle)
            self.inputs["sector1"] = sectorArea(self.get_value("r"), angle)
            self.inputs["arc2"] = self.get_value("circumference") - self.inputs["arc1"]
            self.inputs["sector2"] = self.get_value("ar_cir") - self.inputs["sector1"]
            # Cant do area intersections because havent figured out how to properly label the intersection points 
            # if len(self.Triangle.getMissingVertices()) == 0:
            #     # ar1
            #     weirdArea1 = Polygon(ip2, self.get_value("c"), ip1, self.get_value("v3"))
            #     self.inputs["ar1"] = round(abs(float(weirdArea1.area)) - self.inputs["sector1"], 2)
            #     #ar2
            #     weirdArea2 = Polygon(ip1, self.get_value("c"), ip2, self.get_value("v1"),self.get_value("v2"))
            #     self.inputs["ar2"] = round(abs(float(weirdArea2.area)) - self.inputs["sector2"], 2)


    # Function to solve when only 3 intersection points is chosen
    def threeIps(self):
        # Get center from input sympy geometry library
        if not self.Circle.cirValues["c"] and self.Triangle.GeoT: 
            p = self.Triangle.GeoT.incenter
            self.Circle.cirValues["c"] = (float(p[0]), float(p[1]))
        # Get radius from input sympy geometry library
        if not self.Circle.cirValues["r"] and self.Triangle.GeoT: 
            self.Circle.cirValues["r"] = abs(float(self.Triangle.GeoT.inradius))
        # Get Intersection points from input sympy geometry library
        if self.getIPs() != 3 and self.Triangle.GeoT:  
            points = intersection(self.Triangle.GeoT.incircle, self.Triangle.GeoT)
            s1 = Segment(self.get_value("v2"), self.get_value("v3"))
            s2 = Segment(self.get_value("v1"), self.get_value("v3"))
            s3 = Segment(self.get_value("v2"), self.get_value("v1"))
            # setting ip1
            if len(intersection(s1, points[0])):
                self.set_intersection_points("ip1",float(points[0][0]),float(points[0][1]))
            elif len(intersection(s1, points[1])):
                self.set_intersection_points("ip1",float(points[1][0]),float(points[1][1]))
            elif len(intersection(s1, points[2])):
                self.set_intersection_points("ip1",float(points[2][0]),float(points[2][1]))
            # setting ip2
            if len(intersection(s2, points[0])):
                self.set_intersection_points("ip2",float(points[0][0]),float(points[0][1]))
            elif len(intersection(s2, points[1])):
                self.set_intersection_points("ip2",float(points[1][0]),float(points[1][1]))
            elif len(intersection(s2, points[2])):
                self.set_intersection_points("ip2",float(points[2][0]),float(points[2][1]))
            # setting ip3
            if len(intersection(s3, points[0])):
                self.set_intersection_points("ip3",float(points[0][0]),float(points[0][1]))
            elif len(intersection(s3, points[1])):
                self.set_intersection_points("ip3",float(points[1][0]),float(points[1][1]))
            elif len(intersection(s3, points[2])):
                self.set_intersection_points("ip3",float(points[2][0]),float(points[2][1]))

        self.Circle.solve()
        if self.getIPs() == 3 and self.get_value("r") and self.get_value("circumference") and self.get_value("c"):
            ip1 = self.get_value("ip1")
            ip2 = self.get_value("ip2")
            ip3 = self.get_value("ip3")
            # Code to find arcs and sectors
            s = distanceFormula(ip3[0],ip3[1],ip2[0],ip2[1])
            angle = lawOfCosinesSSS(s, self.get_value("r"),self.get_value("r"))
            self.inputs["arc1"] = arcLength(self.get_value("r"), angle)
            self.inputs["sector1"] = sectorArea(self.get_value("r"), angle)
            # arc/sector 2 
            s = distanceFormula(ip1[0],ip1[1],ip3[0],ip3[1])
            angle = lawOfCosinesSSS(s, self.get_value("r"),self.get_value("r"))
            self.inputs["arc2"] = arcLength(self.get_value("r"), angle)
            self.inputs["sector2"] = sectorArea(self.get_value("r"), angle)
            # arc/sector 3
            s = distanceFormula(ip1[0],ip1[1],ip2[0],ip2[1])
            angle = lawOfCosinesSSS(s, self.get_value("r"),self.get_value("r"))
            self.inputs["arc3"] = arcLength(self.get_value("r"), angle)
            self.inputs["sector3"] = sectorArea(self.get_value("r"), angle)
            # Code to find areas from intersections 
            if len(self.Triangle.getMissingVertices()) == 0:
                # ar1
                weirdArea1 = Polygon(ip2, self.get_value("c"), ip3, self.get_value("v1"))
                self.inputs["ar1"] = round(abs(float(weirdArea1.area)) - self.inputs["sector1"], 2)
                #ar2
                weirdArea2 = Polygon(ip1, self.get_value("c"), ip3, self.get_value("v2"))
                self.inputs["ar2"] = round(abs(float(weirdArea2.area)) - self.inputs["sector2"], 2)
                #ar3
                weirdArea3 = Polygon(ip1, self.get_value("c"), ip2, self.get_value("v3"))
                self.inputs["ar3"] = round(abs(float(weirdArea3.area)) - self.inputs["sector3"], 2)

            

    # Start solving function with a funny name because sometimes in life you gotta entertain yourself 
    def startBeepBoop(self):
        self.Triangle.solve()
        self.Circle.solve()
        # check for Ips 
        num =self.numOfIPs
        if num==1:
            self.oneIps()
        elif num==2:
            self.twoIps()
        elif num==3:
            self.threeIps()


    # Still needed 
    # find vertices from sides and angles
    # algorithm for twoIps
