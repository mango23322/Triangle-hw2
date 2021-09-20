# -*- coding: utf-8 -*-
"""
    Author: Kevin Mengarelli
    Date: 9/14/2021
    Description: SSW 567 Assignment HW01 Unit Test
"""

import unittest
from math import sqrt
from HW01_Kevin_Mengarelli import classify_triangle

# test classify_triangle
class ClassifyTriangleTest(unittest.TestCase):
    def test_right_triangle(self):
        """ test a right triangle, not sorted """
        self.assertEqual(classify_triangle(4,3,5),"Right") 

    def test_equilateral_triangle(self):
        """ Test an equilateral """
        self.assertEqual(classify_triangle(3,3,3), "Equilateral") 

    def test_scalene_triangle(self):
        """ Test a scalene triangle"""
        self.assertEqual(classify_triangle(1,2,3), "Scalene") 

    def test_isosceles_triangle(self):
        """ Test an isosceles triangle """
        self.assertEqual(classify_triangle(3,3,4), "Isosceles") 
        
    def test_right_and_isosceles_triangle(self):
        """ 
        this is a right and isosceles, right triangle has priority
        also tests inputting a float to the function
        """
        # I was actually surprised this one failed. I see now it is due to the float rounding when squaring it isn't perfectly equal to 4
        # but that shows that it was a good thing to test and I would need to fix the code 
        self.assertEqual(classify_triangle(sqrt(2),sqrt(2), 2), "Right")

    def test_not_a_triangle(self):
        """ 
        this one will fail due to weak code (but only on purpose of course)
        this is not a triangle, should result in a failure (I would raise an error in real code)
        """
        with self.assertRaises(ValueError):
            classify_triangle(1,2,9999)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)