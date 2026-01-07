


def max_product_pair(lst):
    lst.sort()
    return max(lst[-1]*lst[-2],lst[0]*lst[1])

print(max_product_pair([2,5,-8,-2,3,1]))

def second(lst):
    lst.sort()
    return lst[2]
print(second([-2,-6,2,5,4,-2,8]))
