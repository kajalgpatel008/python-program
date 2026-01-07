def second_large(n):
    n=list(set(n))
    n.sort()
    return n[-2]
print(second_large([1,5,8,3,9]))


