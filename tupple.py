t=(1,2,5.6,1,11,[1,345,654,765],23,"kajal","Tops",True,False)

print(t)
print(t[5])
t[5].append(400)
print(t)

print(t.index(False))
print(t.count(1))

for i in t:
    print(i)

print(20 in t)
print(2 in t)
