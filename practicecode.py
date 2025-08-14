# reverse a string

def reverse_String(s):
    return s[::-1]

print(reverse_String("kajal"))


def is_prime(n):
    if n%2!= 0:
            for i in range(3,int(n/2)+1,2):
                 if n%i == 0:   
                      print(n,"is not Prime")
                      break
            else :  
                print(n , "is prime")
    else:
        print(n, "is not prime")
n=int(input("Enter N : "))
is_prime(n)
                
def fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while (b<n) :
        print(b,end=" ")
        a,b=b,a+b

fibonacci(254)

def fib(n):
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(40))



