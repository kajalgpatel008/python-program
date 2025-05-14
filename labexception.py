print("start code")

try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))
    c=a/b
    print("Division : ",c)
    c=a*b
    print("Multiplication : ",c)
    c=a-b
    print("Subtraction : ",c)
    c=a+b
    print("Addition : ",c)

except ZeroDivisionError as e:
    print("Exception Caught : ",e)
except ValueError as e:
    print("Exception Caught : ",e)
except IndexError as e:
    print("Exception Caught : ",e)

    
    
    
    
    
    
    






    
