def count_vowels_consonents(s):
    vowels= "aeiouAEIOU"
    v=sum(ch in vowels for ch in s if ch.isalpha())
    c=sum(ch not in vowels for ch in s if ch.isalpha())
    return v,c
print(count_vowels_consonents("Hello Maulik"))
