# https://github.com/alh578/lab10-AH-AH
# Partner 1: Adam Hoshimov
# Partner 2: Adam Hoshimov

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(3, -2), 1)
        self.assertEqual(add(2.5, 3.5), 6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(0, 3), -3)
        self.assertEqual(sub(5,4), 1)
        self.assertEqual(sub(5, -3), 8)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 3), 9)
        self.assertEqual(mul(3, -3), -9)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1, 6), 6)
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(6, -3), -0.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 2), 1)
        self.assertAlmostEqual(log(10, 1000), 3)
        self.assertAlmostEqual(log(10, 21), 1.322219295)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 6)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(6, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(3, -4), 5)
        self.assertAlmostEqual(hypotenuse(3, 3), 4.242640687)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-25)
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 1.414213562)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()