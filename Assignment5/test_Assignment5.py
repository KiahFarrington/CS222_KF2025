import unittest
from Assignment5 import fahrenheit_to_celsius, fibonacci

#extensive testing, hopfully getting edge-cases 
#practicing book's code techniques with methods: each method should have 1 function
class TestAssignment5(unittest.TestCase):
    #testing fahrenheit test
    def test_freezing_point(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    def test_negative_temperature(self):
        # -40F should exactly equal -40C
        self.assertEqual(fahrenheit_to_celsius(-40), -40)

    def test_fahrenheit_float(self):
        # f -> c, gets decimal, have it round out to the nearest 2
        self.assertAlmostEqual(fahrenheit_to_celsius(10), -12.22, places=2)
        
    def test_fahrenheit_string(self):
        with  self.assertRaises(TypeError):
            fahrenheit_to_celsius("freezing")


    # testing fibonacci
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_five(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_seven(self):
        self.assertEqual(fibonacci(7), 13)
        
    def test_fibonacci_ten(self):
        self.assertEqual(fibonacci(10), 55)

            
if __name__ == '__main__':
    unittest.main()