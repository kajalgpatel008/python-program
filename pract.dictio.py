d={123:"kajal",143:5,567:"m","APPLe":245}

print(d)
print(d["APPLe"])

print(d)
d1=d.copy()
print(d1)
print(d.get(123))
print(d.items())
print(d.keys())
d.pop(143)
print(d)
d.popitem()
print(d)
d2={111:"fd",234:"nm"}
d.update(d2)
print(d)
print(d.values())
for i in d:
    print(i)
for i in d:
    print(i ," : ",d[i])
