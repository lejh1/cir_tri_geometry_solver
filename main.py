from inputs import Inputs
from calcs import *

def main():
    inputs = Inputs()
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)
    inputs.set_value("s1", 3)
    inputs.set_value("s2", 3)
    inputs.set_value("a2", 45)
    # inputs.Triangle.simpleRun()
    # inputs.printValues()
    # print(inputs.get_value("a1"))
    # print(inputs.get_value("s1"))
    inputs.Triangle.solve()
    print(inputs.get_all())

    
if __name__ == '__main__':
    main()



