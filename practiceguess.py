import random

num=random.randint(1,20)
while True:                ###while num>0
    
     guess=int(input("Guess A Number Between 1to 20 : "))
     if guess==num:
            print("u guessed a correct number")
            break
     elif guess<num:
            print("u guessed a smaller number")
     elif guess>num:
            print("u entered a greater number")
                    
                
