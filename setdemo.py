s={1,2,10,20,"tops",True,"python",1,2,10}

print(s)
s.add(50)
print(s)
s1={100,200,300,1,2,10,20}
print(s.difference(s1))
print(s.difference_update(s1))
print(s)
print(s1)
s.discard(50)
print(s)
s.add(10)
s.add(50)
print(s1.intersection(s))
print(s)
s.pop()
print(s)
s.remove("tops")
print(s)
print(s.union(s1))
s.update(s1)
print(s)







