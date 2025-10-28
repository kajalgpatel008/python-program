def vowel_conso(s):
    vowels="aeiouAEIOU"
    v=sum(ch in vowels for ch in s if ch.isalpha())
    c=sum(ch not in vowels  for ch in s if ch.isalpha())
    return v,c
print(vowel_conso("kajalmpatel"))

def duplicate(lst):
    num=list(set(lst))
    return num
print(duplicate([6,3,3,1,5,6]))
    

def duplicate(lst):
    result=[]
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print(duplicate([1,3,6,4,4,7,2]))

nums=[1,3,4,5] 
n=5
total=n*(n+1)//2
missing=total-sum(nums)
print(missing)


nums=[1,3,4,5]
n=5
total=n*(n+1)//2
missing=total-sum(nums)
print(missing)
