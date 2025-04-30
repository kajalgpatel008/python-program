import random

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

for i in range(10):
           n=random.choice(l)
           lucky.append(n)
           l.remove(n)
print(l)
print(lucky)
    
