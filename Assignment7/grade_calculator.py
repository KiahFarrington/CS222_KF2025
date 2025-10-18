'''
Define a function that returns the course letter grade for a student given the 
student's average score (between 0 and 100) as a method argument. 
Your function should pass the following unit tests. 
Do not modify the unit test file. 
Raise a TypeError if the method argument is not an int or a float. 
Raise a ValueError if the method argument is either less than 0 or greater than 100.

'''

def calculate_grade(num_grade):

    if not isinstance(num_grade, int) or isinstance(num_grade, float):
        raise TypeError
    elif num_grade < 0 or num_grade > 100:
        raise ValueError
    
    if num_grade >= 90:
        return 'A'
    elif num_grade >= 80:
        return 'B'
    elif num_grade >= 70:
        return 'C'
    elif num_grade >= 60:
        return 'D'
    else:
        return 'F'