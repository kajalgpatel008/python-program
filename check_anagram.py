def check_anagrams(a,b):
    a,b=a.replace("","").lower(),b.replace("","").lower()
    return sorted(a)==sorted(b)

print(check_anagrams("Listen","silent"))
    
