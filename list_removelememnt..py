def remove_element(lst,val):
    i=0
    while i <len(lst):
        if lst[i]==val:
            lst.pop(i)
        else:
            i += 1
    return lst
print(remove_element([1,5,7],1))



def remove_element(lst,val):
    result=[]
    for i in lst:
        if i !=val:
            result.append(i)
    return result
print(remove_element([1,5,7],1))
