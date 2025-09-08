def two_sum(nums,target):
    seen={}
    for i,n in enumerate(nums):
        if target-n in seen:
            return [seen[target-n],i]
        seen[n]=i
    return None
print(two_sum([1,6,4,11,15],5))
