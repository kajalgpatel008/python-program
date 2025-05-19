def fibonacci():

    n=int(input("Enter N : "))
    a,b=0,1
    print(a, end=" ")
    while b<n:
        print(b, end=" ")
        a,b=b,a+b
fibonacci()   


def prime():
    n=int(input("Enter N :"))
    if n%2!=0:
           for i in range(3,int(n/2)+1,2):
             if n%i==0:
                  print(n, "is not prime")
                  break
           else:  
             print(n,"is prime")
    else:
       print(n,"is not prime")

prime()
