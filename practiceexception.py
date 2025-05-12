print("start code")

try:
    
 a=int(input("Enter A : "))
 b=int(input("Enter B : "))

 c=a-b
 print("subtraction : ",c)
 l=[1,2,70,"kajal"]
 index=int(input("Enter index Number to access List variable : "))
 print(l[index])

except ValueError as e:
 print("Exception caught : ",e)
    
print("End Code")




