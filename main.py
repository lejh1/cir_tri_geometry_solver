from inputs import Inputs
def main():
    inputs = Inputs()
    inputs.set_value("a1", 90)
    inputs.set_value("s2", 2)
    inputs.set_value("s3", 2)
    inputs.Triangle.simpleRun()
    inputs.printValues()
    
if __name__ == '__main__':
    main()



