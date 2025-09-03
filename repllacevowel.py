def rep(s):
    vowels="aeiouAEIOU"
    return "".join(chr(ord(ch)+1) if ch in vowels else ch for ch in s)
print(rep("kajalm"))

from collections import Counter
def nonrepeat(s):
    counts=Counter(s)
    for ch in s:
        if counts[ch]==1:
            return ch
    return None
print(nonrepeat("kaaajaalmp"))


def compress_string(s):
    if not s:
        return ""
    result=""
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count += 1
        else:
                result +=s[i-1]+str(count)
                count=1
    result +=(s[-1]+str(count))
    return result
print(compress_string("kkkajaaaalppm"))
        
    
            
