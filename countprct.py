import time

t=int(input("Enter time in seconds :"))

for x in range(t,0,-1):
    seconds=x %60
    minutes=int(x/60) %60
    hours=int(x/3600) %60
    time.sleep(1)

print("Times UP")
