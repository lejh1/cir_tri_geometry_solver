from inputs import Inputs
def main():
    inputs = Inputs()
    inputs.set_value("a1", 90)
    inputs.set_value("s2", 2)
    inputs.set_value("r", 2)
    # inputs.Triangle.simpleRun()
    # inputs.printValues()
    print(inputs.get_value("a1"))
    print(inputs.get_value("s1"))
    print(inputs.Triangle.getMissingSides())

    
if __name__ == '__main__':
    main()



