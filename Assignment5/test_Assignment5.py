import unittest
from Assignment5 import fahrenheit_to_celsius, fibonacci

#testing fahrenheit test
def test_freezing_point():
    assert fahrenheit_to_celsius(32) == 0

def test_negative_temperature():
    # -40F should exactly equal -40C
    assert fahrenheit_to_celsius(-40) == -40

def test_fahrenheit_float():
    # f -> c, gets decimal, have it round out to the nearest 2
    result = fahrenheit_to_celsius(10)
    assert result == -12.22
    
def test_fahrenheit_string():
    with unittest.raises(TypeError):
        fahrenheit_to_celsius("freezing")



# testing fibonacci
def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_five():
    assert fibonacci(5) == 5

def test_fibonacci_seven():
    assert fibonacci(7) == 13
    
def test_fibonacci_seven():
    assert fibonacci(10) == 55

def test_fibonacci_float():
    with unittest.raises(TypeError):
        fibonacci(3.5)

def test_fibonacci_negative():
    with unittest.raises(ValueError):
        fibonacci(-1)