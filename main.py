from inputs import Inputs
from calcs import *

def main():
    inputs = Inputs()
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)
    # inputs.set_value("s1", 3)
    # inputs.set_value("s2", 3)
    # inputs.set_value("a2", 45)
    inputs.set_value("v1", (0,0))
    inputs.set_value("v2", (3,0))
    inputs.set_value("v3", (3,3))
    # inputs.Triangle.simpleRun()
    # inputs.printValues()
    # print(inputs.get_value("a1"))
    # print(inputs.get_value("s1"))
    inputs.Triangle.solve()
    inputs.Triangle.printValues()

    
if __name__ == '__main__':
    main()



