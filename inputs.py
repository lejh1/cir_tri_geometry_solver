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
    
def set_value(name, value): # check if name is valid and if it is then replace it 
    if name in self.inputs:
        self.inputs[name] = value
    elif self.Triangle.checkValueExists(name):
        self.Triangle.setValue(name, value)
    elif self.Circle.checkValueExists(name):
        self.Circle.setValue(name, value)
    else:
        print("That parameter does not exist. Choose a new one.\n")
   
def set_vertex(name, x, y):
    if self.Triangle.checkValueExists(name):
        self.Triangle.setVertex(name, x, y)
    else:
        print("That parameter does not exist. Choose a new one.\n")

def set_center(name, x , y): 
    if self.Circle.checkValueExists(name):
        self.Circle.setVertex(name, x, y)
    else:
        print("That parameter does not exist. Choose a new one.\n")

def set_intersection_points(name, x, y):
    if name in self.inputs:
        self.inputs[name] = (x,y)
    else:
        print("That parameter does not exist. Choose a new one.\n")

