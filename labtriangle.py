for i in range(1,10):
    print(" "*(9-i),str(i)*i)
    

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j),end="")
    print()
        
j=1
for i in range(65,75):
    print(chr(i)*j)
    j=j+1

