def fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    return n
print(fibonacci(25))


n=int(input("Enter N :"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum: ",sum)
    
n=int(input("Enter N :"))         ##while loop
sum=0
while n>0:
    sum=sum+n
    n=n-1
print("sum: ",sum)

count=0
for i in range(1,101):
    if i%2==0:
        print("I :",i)
        count=count+1
    if count==10:
        break

    

        
