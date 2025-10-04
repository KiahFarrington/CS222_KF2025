class Calculator:
    def add(self,x, y):
        return round((x + y), 2)

    def subtract(self, x, y): 
        return round((x - y), 2)
    
    def multiply(self, x, y):
        return round((x * y), 2)
    
    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError ("can't divide by 0")
        
        return round( (x / y), 2)