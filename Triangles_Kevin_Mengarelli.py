# -*- coding: utf-8 -*-
"""
    Author: Kevin Mengarelli
    Date: 9/13/2021
    Description: SSW 567 HW 01
"""

# include
from typing import List
from math import sqrt

def classify_triangle(a: float, b: float, c: float) -> str: 
    ''' takes in three sides of a triangle and return a string for the type of triangle it is
    •	equilateral triangles have all three sides with the same length
    •	isosceles triangles have two sides with the same length
    •	scalene triangles have three sides with different lengths
    •	right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
    '''
    # sides stores all 3 sides and ensure that all 3 sides are stored as a float
    sides: List[float] = [float(a),float(b),float(c)]
    sides.sort() # sort sides smallest to largest

    # if a^2 + b^2 = c^2 then it is a right angle
    if (sides[0]*sides[0] + sides[1]*sides[1] == sides[2] * sides[2]):
        return "Right"
    # if all 3 sides are equal, this is an equilateral triangle
    elif (sides[0] == sides[1] and sides[0] == sides[2]):
        return "Equilateral"
    # if only 2 of the sides are equal, this is an isosceles triangle
    elif (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]):
        return "Isosceles"
    # if all sides are different it is scalene
    else:
        return "Scalene"


print(classify_triangle(3,3,3))
print(classify_triangle(4,3,5))
print(classify_triangle(2,2,3))

    ######################################