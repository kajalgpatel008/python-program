def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")
print(count_vowels("kajal"))

def palindrom(s):
    return s == s[::-1]

print(palindrom("madam"))

def second_large(n):
    n=list(n)
    n.sort()
    return n[-2]

print(second_large([10,4,5,40]))
