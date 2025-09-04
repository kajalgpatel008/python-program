def replace_vowels(s):
    
    vowels="aeiouAEIOU"
    return "".join(chr (ord(ch)+1) if ch in vowels else ch for ch in s)
print(replace_vowels("Kajalmpatel"))
