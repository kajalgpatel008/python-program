from collections import Counter

def count_v_c(s):
    vowels="aeiouAEIOU"
    v=sum(ch in vowels for ch in s if ch.isalpha())
    c=sum(ch not in vowels for ch in s if ch.isalpha())
    return v,c
print(count_v_c("kaajaalmpaateel"))

def c_ana(a,b):
    a,b=a.replace("","").lower(),b.replace("","").lower()
    return sorted(a)==sorted(b)
print(c_ana("Klm","mlak"))

def reverse(s):
    result=""
    for ch in s:
        result =ch+result
    return result
print(reverse("kmpatel"))

def dupli(s):
    result=[]
    for ch in s:
        if ch not in result:
            result.append(ch)
    return "".join(result)
print(dupli("kkkajaaalpp"))

def nonrepeat(s):
    counts=Counter(s)
    for ch in s:
        if counts[ch]==1:
            return ch
    return None
print(nonrepeat("kajalmpaa"))

def compress(s):
    if not s:
        return ""
    result=""
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count +=1
        else:
            result +=s[i-1]+str(count)
            count=1
    result+= s[-1]+str(count)
    return result
print(compress("kajaaa"))
