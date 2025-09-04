from collections import Counter

def first_nonrepeat(s):
        counts=Counter(s)
        for ch in s: 
            if counts[ch]==1:
                return ch
        return None
    
print(first_nonrepeat("kkajla"))
 
