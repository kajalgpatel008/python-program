from functools import reduce
x=lambda a:a+10
print(x(6))

x=lambda a:"Even" if a%2==0 else "Odd"
print(x(25))
print(x(29))
print(x(30))

x=lambda a:"Positive" if a>0 else "Negative"
print(x(25))
print(x(-9))
print(x(0))

x=lambda a:a*a*a
print(x(5))
print("cube of 5 is : ",x(5))

x=[1,2,3,4,5,6,7,8,9,10]
y=filter(lambda x:x%2==0,x)
print(list(y))

x=[1,2,3,4,5,6,7,8,9,10]
y=map(lambda x:x*3,x)
print(list(y))

x=[1,2,3,4]
y=reduce(lambda x,y:x*y,x)

print((y))






