#1
#Input degree: 15
#Output radian: 0.261904

import math

pi = math.pi

def convertToRadian(x):
    return (x * pi) / 180

print(convertToRadian(15))


#2
""" Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5 """

def calcAreaOfTrapezoid(a, b, h):
    return ((a + b) / 2) * h

print(calcAreaOfTrapezoid(5, 6, 5))


#3
""" Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625 """

import math
pi = math.pi

def calcArea(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

print(calcArea(4, 25))


#4
import math

def areaOfParallelogram(a, b):
    return a * b

print(areaOfParallelogram(5, 6))