def chunk_list(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]
print(chunk_list([1,2,4,5,3,7,6,9],2))
    
