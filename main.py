from inputs import Inputs
from calcs import *
from sympy.geometry import intersection 


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
    points = intersection(inputs.Triangle.GeoT.incircle, inputs.Triangle.GeoT)
    print(points)
    inputs.set_intersection_points("ip1",float(points[0][0]),float(points[0][1]))
    inputs.set_intersection_points("ip2",float(points[1][0]),float(points[1][1]))
    inputs.set_intersection_points("ip3",float(points[2][0]),float(points[2][1]))
    inputs.printValues()
    # print(inputs.Triangle.GeoT.incircle)
    # print(float(inputs.Triangle.GeoT.inradius))
    # print(float(intersection(inputs.Triangle.GeoT.incircle, inputs.Triangle.GeoT)[0][0]))


    
if __name__ == '__main__':
    main()



