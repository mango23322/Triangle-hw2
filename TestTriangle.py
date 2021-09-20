# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(3,3,4),'Isosceles','3,3,4 should be an Isosceles triangle')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(4,3,3),'Isosceles','4,3,3 should be an Isosceles triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be a Scalene triangle')            

    def testStringInput(self):
        self.assertEqual(classifyTriangle('one','two','three'),'InvalidInput','Must input integers')

    def testFloatInput(self):
        self.assertEqual(classifyTriangle(1.0,1.0,1.0),'InvalidInput','Must input integers')
   
    def testLargeInput(self):
        self.assertEqual(classifyTriangle(250, 250, 250),'InvalidInput','Must be < 200')
    
    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(0, 0, 0),'InvalidInput','Must be > 0')

    def testNonTriangle(self):
        self.assertEqual(classifyTriangle(1,1,10),'NotATriangle','1, 1, 10 is not a valid triangle')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

