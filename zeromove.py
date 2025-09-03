l=[1,0,0,2,4,6,0,0,8]

for i in l:
   if i==0:
       l.remove(i)
       l.append(i)
print(l)
