file=open("tops.txt","w")
file.write("This is file management demo using python.")
file.write("This is python file.")
file.write("This is demofile.")

file.close()
print("file Written Successfully")

file=open("tops.txt","r")
print(file.read())
file.close()

print("---------------------------------")
