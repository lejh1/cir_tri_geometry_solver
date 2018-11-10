from inputs import Inputs
from calcs import *

def main():
    inputs = Inputs()
    inputs.set_value("a1", 90)
    inputs.set_value("ip3", (2,3))
    inputs.set_value("ip2", (3,3))
    inputs.set_value("ip1", (2,4))
    # inputs.Triangle.simpleRun()
    # inputs.printValues()
    print(inputs.get_value("a1"))
    print(inputs.get_value("s1"))
    print(inputs.getIPs())
    print(distanceFormula(inputs.get_value("ip1")[0],inputs.get_value("ip1")[1],inputs.get_value("ip2")[0],inputs.get_value("ip2")[1]))

    
if __name__ == '__main__':
    main()



