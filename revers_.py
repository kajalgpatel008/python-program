def reverse(s):
    result=""
    for ch in s:
        result=ch+result
    return result
print(reverse("kajal"))


def second_larg(nums):
    nums=list(set(nums))
    nums.sort()
    return nums[-2]
print(second_larg([1,5,7,3,8]))

""" prime number """

n=int(input("Enter N :"))
if n%2 !=0:
      for i in range(3,int(n/2)+1,2):
        if n%i==0:
             print(n,"is not prime")
             break
      else: 
         print(n,"is prime")            ## else should be outside of loop
else: 
    print(n,"is not prime")


def factorial(n):
    if n==0 or n==1 :
        return 1
    fact=""
    return n*factorial(n-1)
print(factorial(3))
