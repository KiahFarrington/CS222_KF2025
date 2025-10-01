class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self,x, y): #Returns the sum of x and y
        return x + y

    def subtract(self, x, y): #Returns the result of subtracting y from x
        return y - x

calc = Calculator(8,0)
print(calc.add())
print(calc.subtract())