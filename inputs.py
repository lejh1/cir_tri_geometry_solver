# Hold all possible input values 
# Uses Triangle and Circle objects
from sympy.geometry import intersection 
from triangle import Triangle
from circle import Circle
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
        "ar3":0
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
        return new_dict

    # Returns a list of all the not solvable parameters
    def getNotSolvable(self):
        notS = list()
        d = self.get_all()
        for key, value in d.items():
            if not value:
                notS.append(key)
        if self.numOfIPs == 1:
            notS.remove("ip2")
            notS.remove("ip3")
        elif self.numOfIPs == 2:
            notS.remove("ip3")
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
        if not self.get_value("ip1") and self.Circle.geoC and self.Triangle.GeoT:
            point = intersection(self.Circle.geoC, self.Triangle.GeoT)
            self.set_intersection_points("ip1", float(point[0]), float(point[1]))
        print(1)
    
    # Function to solve when only 2 intersection points is chosen
    def twoIps(self):
        print(1)
    
    # Function to solve when only 3 intersection points is chosen
    def threeIps(self):
        num = len(self.Triangle.getMissingVertices())
        # Get radius from input sympy geometry library
        if not self.Circle.cirValues["c"] and not num and self.Triangle.GeoT: 
            p = self.Triangle.GeoT.incenter
            self.Circle.cirValues["c"] = (float(p[0]), float(p[1]))
        # Get radius from input sympy geometry library
        if not self.Circle.cirValues["r"] and not num and self.Triangle.GeoT: 
            self.Circle.cirValues["r"] = float(self.Triangle.GeoT.inradius)
        # Get Intersection points from input sympy geometry library
        if self.getIPs() != 3 and not num and self.Triangle.GeoT:  
            points = intersection(inputs.Triangle.GeoT.incircle, inputs.Triangle.GeoT)
            self.set_intersection_points("ip1",float(points[0][0]),float(points[0][1]))
            self.set_intersection_points("ip2",float(points[1][0]),float(points[1][1]))
            self.set_intersection_points("ip3",float(points[2][0]),float(points[2][1]))
        self.Circle.solve()
        print(1)

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