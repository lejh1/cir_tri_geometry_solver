import math
# def lawOfSinesASA():


def lawOfCosinesSSS(a,b,c): # a is the side the cooresponds to the angle we want to find
    return round(math.degrees(math.acos(((-pow(a,2))+pow(b,2)+pow(c,2))/(2*b*c))),2)

def lawOfCosinesSAS(A,b,c): # a is the angle that cooresponds to the side we want to find
    return round(math.sqrt(pow(b,2)+pow(c,2)-(2*b*c*math.cos(math.radians(A)))),2)

def lawOfSinesSSA(a,b,A): # Finds Angle B
    return round(math.degrees(math.asin(((b*math.sin(math.radians(A)))/a))),2) # may need to adjust for boundary error 

def lawOfSinesAAS(A,b,B): # Finds Side a
    return round((b*math.sin(math.radians(A)))/math.sin(math.radians(B)),2) # may need to adjust for boundary error 

def distanceFormula(x1,y1,x2,y2):
    return math.hypot(x2-x1, y2-y1)

# Finds the Area of the triangle 
def heronsFormula(s1,s2,s3):
    s = float((s1+s2+s3))/2
    return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))