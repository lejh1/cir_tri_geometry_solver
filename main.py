from inputs import Inputs
from calcs import *

def main():
    inputs = Inputs()
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)

    inputs.set_value("v3", (3,0))
    inputs.set_value("v2", (3,3))
    inputs.set_value("v1", (0,0))
    # inputs.Triangle.simpleRun()
    # inputs.printValues()
    # print(inputs.get_value("a1"))
    # print(inputs.get_value("s1"))
    print(inputs.Triangle.solve())
    print(inputs.get_all())

    
if __name__ == '__main__':
    main()



