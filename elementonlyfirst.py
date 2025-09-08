def list_difference(a,b):
    return [x for x in a if x not in b]
print(list_difference([1,3,2],[2,4,1,6]))


def list_difference(a,b):
    return [x for x in b if x not in a]
print(list_difference([1,3,2],[2,4,1,6]))
