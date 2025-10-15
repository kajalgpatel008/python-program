def flatten_nested(lst):
    return [item for sub in lst for item in sub]
print(flatten_nested([[1,3,4],[5,3,4,7]]))
 

def move_zero(lst):
    nonzeros= [item for item in lst if item!=0]
    return nonzeros  + [0]*(len(lst)-len(nonzeros))
print(move_zero([1,3,0,0,0,2,0,5]))

