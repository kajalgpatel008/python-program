import random

file=open("random.txt","w")
file.write("This is Random File Demo.")

print(random.randint(1,50))
num=random.randint(1,50)


for i in range(10):
    print(random.randint(1,50))

print("File Written Successfully")
file.close()

file=open("random.txt","r")
print(file.read())
file.close()
