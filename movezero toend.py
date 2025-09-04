l=[0,3,5,7,0,0,4,0,5,0]

for item in l:
    if item==0:
        l.remove(item)
        l.append(item)

print(l)
