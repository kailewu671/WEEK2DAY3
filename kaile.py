

import math 

def circle():
    radius = float(input("Enter the radius of the circle : "))
    circumference =  2 * math.pi * radius
    print("Circumference of the circle is : %.2f" % circumference)

def squarefoot():
    length = float(input("Enter the length of house ")) 
    width = float(input("Enter the width of house"))
    area = length * width 
    print(f"Square footage of house is: {area}")

    