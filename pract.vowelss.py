def vowels(s):
    return sum(1 for ch in s.lower() or s.upper() if ch in 'aeiou')
print(vowels("Interview"))
