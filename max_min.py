def max_min_from_string(s):
    nums=[int(x) for x in s.split(",")]
    return min(nums),max(nums)
print(max_min_from_string("3,5,1,9,2"))

