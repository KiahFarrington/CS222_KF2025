import math

#constants
HOTDOGPACKAGE = 10
BUNSPACKAGE = 8

def main():
    people = int(input("How many people are there?: "))
    per_person = int(input("And how many hot dogs should each person get?: "))
    
    hot_dogs_needed = people * per_person
    
    buns_packages = math.ceil(hot_dogs_needed / BUNSPACKAGE)
    dogs_packages = math.ceil(hot_dogs_needed / HOTDOGPACKAGE)
    
    buns_bought = buns_packages * BUNSPACKAGE
    dogs_bought = dogs_packages * HOTDOGPACKAGE
    
    buns_leftover = buns_bought - hot_dogs_needed
    dogs_leftover = dogs_bought - hot_dogs_needed
    
    print("The minimum number of packages of hot dog buns required are: ", buns_packages)
    print("The minimum number of packages of hot dogs required are: ", dogs_packages)
    print("Leftover hot dogs: ", dogs_leftover)
    print("Leftover hot dog buns: ", buns_leftover)
    
main()