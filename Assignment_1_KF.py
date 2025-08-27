#Calculate your BMI and output it
def problem1():
    print("Problem #1")
    weight = float(input("To Calculate your BMI, enter your weight(in pounds): "))
    height = float(input("Now enter you height(in inches): "))
    BMI = (weight * 703) / height ** 2
    
    if BMI >= 25:
        print("Your BMI is", BMI, "and is considered overweight")       
    elif BMI >= 18.5:
        print("Your BMI is", BMI, "and is considered healthy")
    else:
        print("Your BMI is", BMI, "and is considered underweight")
   
    
#sum of even numbers in the range 2-100  
def problem2():
    print("\nProblem #2")
    sum = 0
    for num in range(2, 101):
        if num % 2 == 0:
            sum += num
        
    print("The total sum of even numbers under 100 (inclusive) is: {}".format(sum))


# sum of odd numbers in the range a-b (given by user)
def problem3():
    print("\nProblem #3")
    sum = 0
    a = int(input("a: "))
    b = int(input("b: "))
    
    for num in range(a,b):
        if num % 2 != 0:
            sum += num
        
    print("The total sum of odd number is in the range {}-{} is {}".format(a, b-1,sum))
    

#Ask for current stock and target stock, once current hits target stock price, "Shares can be sold now"
def problem4():
    print("\nProblem #4") 
    target = float(input("Target stock price: "))
    current = float(input("Current stock price: "))
    while target > current:
        current = float(input("Current stock price: "))
    
    print("Shares can be sold now")   
    
    
#Callculate full-time tuition interest, with year 1 starting @ $8,000, and growing by 3%   
def problem5():
   print("\nProblem #5")  
   tuition = 8000
   increased_tuition = tuition
   print("Full time tuition cost\nyear 1: $",tuition)
   
   for num in range(2,6):
       increased_tuition = increased_tuition * 1.03
       print("year {}: ${:.2f}".format(num , increased_tuition)) #{:.2f} to limit to 2 decimal spots for money
   

problem1()
problem2()
problem3()
problem4()
problem5()