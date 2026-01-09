
def palindrom(s):
    result=""
    return s==s[::-1]
print(palindrom("madam"))

import random

l=[]
lucky=[]
for i in range(1,101):
    l.append(i)
for i in range(1,11):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)
print(l)
print(lucky)

num=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 to 20 : "))

    if guess==num:
        print("you guessed correct number")
        break
    elif guess>num:
        print("you guessed greater number")
    elif guess<num:
        print("you guessed smaller number")
        
