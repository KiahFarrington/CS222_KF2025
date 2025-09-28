# Unit_test_notes/test_utils.py
import unittest           # Built-in unit testing framework
from Unit_test_notes import utils   # The module we’re testing

class TestUtils(unittest.TestCase):
    """
    Each method in this class is an independent TEST CASE.
    Inheriting from unittest.TestCase gives us access to
    dozens of assertion methods (assertEqual, assertTrue, etc.).
    """

    # ---------- Fixtures ----------
    def setUp(self):
        """
        setUp() runs BEFORE EVERY test method.
        Use it to create objects or data shared across tests.
        Each test gets a *fresh* setup to avoid cross-test contamination.
        """
        self.sample_numbers = [1, -3, 10, 5, 0] # self.sample_numbers is now an instance variable of the test class.

    def tearDown(self):
        """
        tearDown() runs AFTER EVERY test method.
        Use it for cleanup (closing files, deleting temp data).
        Here it’s just for demonstration.
        """
        self.sample_numbers = None # dont always need to do this


    # ---------- Tests for is_even ----------
    def test_is_even_with_even_number(self): #Basic case: even integer should return True
        self.assertTrue(utils.is_even(10))    # True check

    def test_is_even_with_odd_number(self): #Odd integer should return False
        self.assertFalse(utils.is_even(7))    # False check

    def test_is_even_with_invalid_type(self):
        """
        Passing a non-int should raise TypeError.
        We use assertRaises as a context manager to confirm
        the *type* of exception—not just any error.
        """
        with self.assertRaises(TypeError):
            utils.is_even(3.5)

    # ---------- Tests for factorial ----------
    def test_factorial_of_positive(self):# assertEqual compares actual vs expected.
        self.assertEqual(utils.factorial(5), 120)

    def test_factorial_edge_cases(self):
        """
        Factorial of 0 or 1 should both be 1.
        We can group related checks in one method if they
        represent the same logical behavior.
        """
        self.assertEqual(utils.factorial(0), 1)
        self.assertEqual(utils.factorial(1), 1)

    def test_factorial_negative_input(self): # Negative numbers should raise ValueError.
        with self.assertRaises(ValueError): # We test for correctness of error handling.
            utils.factorial(-3)

    # ---------- Tests for max_min ----------
    def test_max_min_regular_list(self): #Check that it returns a tuple (max, min).
        self.assertEqual(utils.max_min(self.sample_numbers), (10, -3))

    def test_max_min_empty_list(self): # Empty list should raise ValueError.
        with self.assertRaises(ValueError):
            utils.max_min([])



    # ---------- Advanced Example ----------
    def test_is_even_multiple_inputs_subtests(self):
        """
        Subtests allow looping through many inputs
        without stopping at the first failure.
        Useful for parameterized checks.
        """
        cases = [(2, True), (3, False), (0, True)]
        for n, expected in cases:
            with self.subTest(n=n):
                self.assertEqual(utils.is_even(n), expected)


    # ---------- Skipping Example ----------
    @unittest.skip("Demonstration of skipping a test you haven't implemented yet")
    def test_future_feature(self):
        pass

# Standard boilerplate to run tests directly with: python test_utils.py
if __name__ == '__main__':
    unittest.main(verbosity=2)
    # verbosity=2 gives more detailed output
    
'''
# ==================================================================
# UNITTEST ASSERT / ERROR CHECK CHEAT SHEET
# ==================================================================
# 2 values are EXACTLY the same
    self.assertEqual(result, expected)


# 2 values = different
    self.assertNotEqual(result, unexpected)


#2 floating-point numbers are almost equal
    self.assertAlmostEqual(a, b, places=7)  # default 7 decimal places
    

#Check if something is True / False
    self.assertTrue(condition)
    self.assertFalse(condition)


#Check if two variables are literally the SAME object in memory
    self.assertIs(a, b)
    self.assertIsNot(a, b)   # opposite


# Check if something is (or isnt) None
    self.assertIsNone(x)
    self.assertIsNotNone(x)


# Check if an item exists inside a container (list, string, dict keys, etc.)
    self.assertIn(item, container)
    self.assertNotIn(item, container)


# Check that code raises a specific error
    with self.assertRaises(ValueError):
        function_that_should_fail()
     OR shorter function form:
    self.assertRaises(ValueError, function_that_should_fail, arg1, arg2)

Tip: Always pick the *most specific* assertion you can.
       Example: use assertIn(...) instead of assertTrue(x in y)
==================================================================
'''