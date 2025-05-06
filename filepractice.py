file=open("prime.txt","w")
file.write("This is Prime number")

n=int(input("Enter N : "))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"Is Not Prime")
            break
    else:
        print(n,"Is Prime")
else:
    print(n, "Is Not Prime")

file.close()

file=open("prime.txt","w+")
file.write("This is Python program")
print("current position : ",file.tell())
file.seek(0)
print("This file is w+ mode :", file.read())
file.close()

file=open("prime.txt","r+")
file.write("python is versatile p.g")
file.seek(0)
print("This file is r+ mode :", file.read())
file.close()



