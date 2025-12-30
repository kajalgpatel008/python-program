def factorial(n):
    if n==0 or n==1 :
        return 1
    return n*  factorial(n-1)
print(factorial(5))

def second_large(num):
    num=list(set(num))
    num.sort()
    return num[-1]
print(second_large([1,4,6,2]))

def reverse(s):
    result=""
    for ch in s:
        result = ch+result
    return result
print(reverse("kajalm"))



def second_large(t):
    num=sort(set(t))
    return num[-2] if len(t)>=2 else None
print(second_large([1,5,6,2]))

