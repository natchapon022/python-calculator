import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add1(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(-1, 2), 1)
        
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(-2, 1), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(7, 2), 1)
        self.assertEqual(self.calc.modulo(9, 0), 9)

if __name__ == '__main__':
    unittest.main()