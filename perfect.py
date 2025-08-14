n=int(input("Enter number: "))

sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("The number is Perfect number")
else:
    print("the number is not perfect number")
    
    
