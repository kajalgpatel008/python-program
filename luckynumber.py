import random

#print(random.randint(1,100))
#print(random.choice([1,2,10,20,"tops","python"]))

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
