def rotate_list(lst,k):
    k%=len(lst)
    return lst[-k:]+lst[:-k]
print(rotate_list([1,3,4,2,8],2))


