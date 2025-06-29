import re

if re.search("python","niki is registered in Python technology"):
  print("Result match !!!")
else:
  print("Result Not Found !!")



# use of finditer


name="Python is world's best programming language "
for i in re.finditer("world's",name):
  ans=i.span()
  print(ans)


# Email pattern
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "test@example.com"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
