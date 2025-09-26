def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit- 32) * 5.0/9.0
    return round(celsius, 2)
    
      
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    a = 0 
    b = 1
    for count in range(n - 1):
        temp = b
        b = a + b
        a = temp
         
    return b
    
    
def main():
    #main call for converting temperature
    tempature = float(input("Input Fahrenheit temperature: ")) 
    tempature = fahrenheit_to_celsius(tempature)
    print("In Celsius it is:", tempature , "°C")
    
    #main call for  fibonacci
    num = int(input("Input the nth Fibonacci number you want in the sequence: "))
    fibResult = fibonacci(num)
    print("It is:", fibResult)

if __name__ == "__main__": 
    main()