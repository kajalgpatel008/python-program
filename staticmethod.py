class Calculator:

   
    def add(x,y):
        return x+y
    
    @staticmethod
    def multiply(x,y):
        return x * y

print(Calculator.add(5,3))
print(Calculator.multiply(5,5))
