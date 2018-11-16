from inputs import Inputs
from calcs import *
from ast import literal_eval 
import sys
# from sympy.geometry import intersection 


def main():
    inputs = Inputs()
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)
    # inputs.set_value("a1", 90)
    # inputs.set_value("s1", 3)
    # inputs.set_value("s2", 3)
    # # inputs.set_value("a2", 45)
    # inputs.set_value("v1", (0,0))
    # inputs.set_value("v2", (3,0))
    # inputs.set_value("v3", (3,3))
    # inputs.numOfIPs= 3 # number of intersection points
    # inputs.startBeepBoop()
    # inputs.printValues()
    # print(inputs.getNotSolvable())
    menuInputs()


def menuInputs():
    inputs = Inputs()
    sel = eval(input("Which problem would you like to solve? (1,2,3): "))
    if sel not in [1,2,3]:
        sys.exit("Error incorrect value. Exiting")
    elif sel == 1:
        inputs.numOfIPs = 1
        while(True):
            print("*** v1, v2, v3, s1, s2, s3, a1, a2, a3, ar_tri, per_tri, r, c, d, ar_cir, circumference ***")
            sel = input("Please select a parameter to enter from the above list or type \"exit\" to quit: ")
            if sel not in ["exit","v1", "v2", "v3", "s1", "s2", "s3", "a1", "a2", "a3", "ar_tri", "per_tri", "r", "c", "d", "ar_cir" , "circumference"]:
                print("Parameter does not exist, try again!")
            elif sel == "exit":
                break
            elif sel in ["v1", "v2", "v3", "c"]:  
                val = input("Input value for "+sel+" coordinate in form of \"(#,#)\": ")
                if sel == "c":
                    try:
                        inputs.set_center(sel,literal_eval(val)[0],literal_eval(val)[1])
                        print("Value for "+sel+" was entered!")
                    except Exception as e:
                        print("Input form was wrong!")
                else:
                    try:
                        inputs.set_vertex(sel,literal_eval(val)[0],literal_eval(val)[1])
                        print("Value for "+sel+" was entered!")
                    except Exception as e:
                        print("Input form was wrong!")
            else:
                val = input("Input value for "+sel+": ")
                inputs.set_value(sel,float(val))

    elif sel == 2:
        inputs.numOfIPs = 2
        while(True):
            print("*** v1, v2, v3, s1, s2, s3, a1, a2, a3, ar_tri, per_tri, r, c, d, ar_cir, circumference, ip1, ip2, arc1, arc2, ar1, ar2 ***")
            sel = input("Please select a parameter to enter from the above list or type \"exit\" to quit: ")
            if sel not in ["exit","v1", "v2", "v3", "s1", "s2", "s3", "a1", "a2", "a3", "ar_tri", "per_tri", "r", "c", "d", "ar_cir" , "circumference", "ip1", "ip2", "arc1", "arc2", "ar1", "ar2"]:
                print("Parameter does not exist, try again!")
            elif sel == "exit":
                break
            elif sel in ["v1", "v2", "v3", "c"]:  
                val = input("Input value for "+sel+" coordinate in form of \"(#,#)\": ")
                if sel == "c":
                    try:
                        inputs.set_center(sel,literal_eval(val)[0],literal_eval(val)[1])
                        print("Value for "+sel+" was entered!")
                    except Exception as e:
                        print("Input form was wrong!")
                else:
                    try:
                        inputs.set_vertex(sel,literal_eval(val)[0],literal_eval(val)[1])
                        print("Value for "+sel+" was entered!")
                    except Exception as e:
                        print("Input form was wrong!")
            elif sel in ["ip1","ip2","ip3"]:
                val = input("Input value for "+sel+" coordinate in form of \"(#,#)\": ")
                try:
                    inputs.set_intersection_points(sel,literal_eval(val)[0],literal_eval(val)[1])
                    print("Value for "+sel+" was entered!")
                except Exception as e:
                    print("Input form was wrong!")
            else:
                val = input("Input value for "+sel+": ")
                inputs.set_value(sel,float(val))
                
    elif sel == 3:
        inputs.numOfIPs = 3
        while(True):
            print("*** v1, v2, v3, s1, s2, s3, a1, a2, a3, ar_tri, per_tri, r, c, d, ar_cir, circumference, ip1, ip2, ip3, arc1, arc2, arc3, ar1, ar2, ar3 ***")
            sel = input("Please select a parameter to enter from the above list or type \"exit\" to quit: ")
            if sel not in ["exit","v1", "v2", "v3", "s1", "s2", "s3", "a1", "a2", "a3", "ar_tri", "per_tri", "r", "c", "d", "ar_cir" , "circumference", "ip1", "ip2", "ip3", "arc1", "arc2", "arc3", "ar1", "ar2", "ar3"]:
                print("Parameter does not exist, try again!")
            elif sel == "exit":
                break
            elif sel in ["v1", "v2", "v3", "c"]:  
                val = input("Input value for "+sel+" coordinate in form of \"(#,#)\": ")
                if sel == "c":
                    try:
                        inputs.set_center(sel,literal_eval(val)[0],literal_eval(val)[1])
                        print("Value for "+sel+" was entered!")
                    except Exception as e:
                        print("Input form was wrong!")
                else:
                    try:
                        inputs.set_vertex(sel,literal_eval(val)[0],literal_eval(val)[1])
                        print("Value for "+sel+" was entered!")
                    except Exception as e:
                        print("Input form was wrong!")
            elif sel in ["ip1","ip2","ip3"]:
                val = input("Input value for "+sel+" coordinate in form of \"(#,#)\": ")
                try:
                    inputs.set_intersection_points(sel,literal_eval(val)[0],literal_eval(val)[1])
                    print("Value for "+sel+" was entered!")
                except Exception as e:
                    print("Input form was wrong!")
            else:
                val = input("Input value for "+sel+": ")
                inputs.set_value(sel,float(val))

    inputs.startBeepBoop()
    print("Solved Terms:")
    inputs.printValues()
    print("Unsolvable Terms:")
    print(inputs.getNotSolvable())



    
if __name__ == '__main__':
    main()