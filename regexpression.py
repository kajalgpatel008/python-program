import re

Nameage="""Rany is 23 and Jeny is 65, Tom is 25 and Roy is 42 """
age=re.findall(r'\d{1,3}',Nameage)
name=re.findall(r'[A-Z][a-z]*',Nameage)

Age={}
a=0

for i in name:
  Age[i] =age[a]
  a+=1
    
print(Age)
