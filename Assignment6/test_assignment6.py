import unittest
from Assignment6.Assignment6_calculator import Calculator

class test_Calculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_basic_add(self):
        self.assertEqual(self.calc.add(2,16), 18)

    def test_negative_add(self):
        self.assertEqual(self.calc.add(-2,2), 0) 
    
    def test_decimals_add(self):
        self.assertAlmostEqual(self.calc.add(5.23,1.6),6.83)  
    
    def test_correct_type_add(self):
       with self.assertRaises(TypeError):
            self.calc.add(5, "hello")



    def test_basic_sub(self):
        self.assertEqual(self.calc.sub(8,9), 1)

    def test_negative_sub(self):
        self.assertEqual(self.calc.sub(20,1), -19)

    def test_decimals_sub(self):
        self.assertAlmostEqual(self.calc.sub(4.25,9.45), 5.20)  
    
    def test_correct_type_sub(self):
       with self.assertRaises(TypeError):
            self.calc.sub(5, "hello")
