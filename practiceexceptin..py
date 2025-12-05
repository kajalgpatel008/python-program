print("start code")

try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))
    c=a/b
    print("Division : ",c)
    l=[1,2,3,4,5]
    index=int(input("enter index Number To Access List Variable : "))
    print(l[index])
except Exception as e:
    print("Exception Caught : ",e)
print("End Code")


    
