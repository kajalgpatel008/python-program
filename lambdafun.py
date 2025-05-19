from functools import reduce 

x=lambda a:a+20

print(x(5))

def cube(x):
    return x*x*x

print("cube of ",5 ,"Is : ",cube(5))

y=lambda b:b*b*b
print("cube of ",5,"Is : ",y(5))

z=lambda c:"Even" if c%2==0 else "Odd"
print(z(4))
print(z(5))

n=[1,2,3,4,5,6,7,8,9,10,20,21,22,23,24,35,56,67,78,89,90]

even=filter(lambda x:x%2==0,n)
print(list(even))


n=[1,2,3,4,5,6,7,8,9,10,20,21,22,23,24,35,56,67,78,89,90]

even=map(lambda x:x*3,n)
print(list(even))

n1=[1,2,3,4,5,6]
n2=reduce(lambda x,y:x*y,n1)

print(n2)


