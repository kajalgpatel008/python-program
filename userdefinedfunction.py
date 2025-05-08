#function with no argument & no return value

def printline():                   ###L is capital
    print("*"*50)

printline()
print("Welcome to user defined function in python")
printline()

#function with argument & no return value

def add(a,b):
    print("Addition : ",a+b)

printline()
add(10,20)
printline()

#function with argument &  return value

def sub(a,b):
    return a-b

printline()
x=sub(10,20)
print("Subtraction : ",x)
printline()
