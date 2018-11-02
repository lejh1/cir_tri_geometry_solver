import math
# def lawOfSinesASA():


def lawOfCosinesSSS(a,b,c): # a is the side the cooresponds to the angle we want to find
    return round(math.degrees(math.acos(((-pow(a,2))+pow(b,2)+pow(c,2))/(2*b*c))),2)

def lawOfCosinesSSA(A,b,c): # a is the angle that cooresponds to the side we want to find
    return round(math.sqrt(pow(b,2)+pow(c,2)-(2*b*c*math.cos(math.radians(A)))),2)