import json

#Create an empty dictionary to store user input
users_data= {}

#Accept user input

user_data["name"]=input("Enter user's name: ")
user_data["age"]=int(input("Enter user's age: "))
user_data["city"]=input("Enter user's city: ")

 

# open a JSON file in write mode
with open("user_data.json", "w") as file:
    #write the  dictionary to the file in JSON format
    json.dump(user_data, file, indent=4)

print("Data added ||")
    

