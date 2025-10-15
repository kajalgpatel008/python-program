def title(s):
    words=s.split()
    return  " ".join(w[0].upper()+w[1:].lower() if w else "" for w in words)
print(title("kajal m patel"))


def max_min(s):
    nums=[int(x) for x in s.split(",")]
    return max(nums),min(nums)
print(max_min("2,7,8,4,6,9"))


def max_min(s):
    nums=[int(x) for x in s.split(',')]
    return max(nums),min(nums)
print(max_min("9,5,7,3,2,6,6")) 

