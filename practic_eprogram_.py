def check_anagram(a,b):
    a,b=a.replace("","").lower(),b.replace("","").lower()
    return sorted(a)==sorted(b)
print(check_anagram("Silent","Listen"))

def reverse_string(s):
    result=""
    for ch in s:
        result=ch +result
    return result
print(reverse_string("kajalm"))

def duplicate(s):
    result=[]
    for ch in s:
        if ch not in result:
            result.append(ch)
    return "".join(result)
print(duplicate("kajalmpatelaaal"))
