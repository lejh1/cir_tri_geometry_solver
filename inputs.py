# Hold all possible input values 
# Uses Triangle and Circle objects
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
        self.Triangle = Triangle()
        self.Circle = Circle()
    
    def set_value(self, name, value): # check if name is valid and if it is then replace it 
        if name in self.inputs:
            self.inputs[name] = value
        elif self.Triangle.checkValueExist(name):
            self.Triangle.setValue(name, value)
        elif self.Circle.checkValueExist(name):
            self.Circle.setValue(name, value)
        else:
            print("That parameter does not exist. Choose a new one.\n")
    
    def set_vertex(self, name, x, y):
        if self.Triangle.checkValueExist(name):
            self.Triangle.setVertex(name, x, y)
        else:
            print("That parameter does not exist. Choose a new one.\n")

    def set_center(self, x , y): 
            self.Circle.setCenter(x, y)

    def set_intersection_points(self, name, x, y):
        if name in self.inputs:
            self.inputs[name] = (x,y)
        else:
            print("That parameter does not exist. Choose a new one.\n")

    def printValues(self):
        print(self.inputs)
        self.Triangle.printValues()
        self.Circle.printValues()
    
    def get_value(self, name):
        if name in self.inputs:
            return self.inputs[name] 
        elif self.Triangle.checkValueExist(name):
            return self.Triangle.getValue(name)
        elif self.Circle.checkValueExist(name):
            return self.Circle.getValue(name)
        else:
            print("That parameter does not exist. Choose a new one.\n")
    
    def get_all(self):
        new_dict = self.inputs
        new_dict.update(self.Triangle.triValues)
        new_dict.update(self.Circle.cirValues)
        return new_dict

    def getIPs(self):
        count = 0
        for i in range(1,4):
            s = "ip" + str(i)
            if self.inputs[s]:
                count += 1
        return count

    def startBeepBoop(self):
        if getIps()==1:

            print(1)
