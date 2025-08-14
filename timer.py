import time

def countdown(t):
    while t>0:
        print(t)
        t=t-1
        time.sleep(1)

    print("Time's Up")
print("How many seconds to count down?")
seconds=input("Enter the seconds :")
while not seconds.isdigit():
    print("That was not an integer. please Enter an integer")
    seconds=input("Enter the seconds :")
seconds=int(seconds)
countdown(seconds)
