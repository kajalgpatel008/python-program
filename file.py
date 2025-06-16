import random

data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")

data.close()

data=open("data.txt","r")
l=data.read()
print(l)
data.close()
        
        

               
 
