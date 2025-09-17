d={101:"Kajal",345:"Henil",909:"Jigar"}

print(d)
print(d[345])
print(d.get(909))
print(d.items())
print(d.keys())
d.pop(909)
print(d)
d.popitem()
print(d)
d1={111:"Henil",222:"jigar",333:"Gaurav",444:"Shubham"}
d.update(d1)
print(d)
print(d.values())
d2=d.copy()
print(d2)

for i in d:
    print(i, " : ",d[i])
d[222]="Shreyash"
print(d)


