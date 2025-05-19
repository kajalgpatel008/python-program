from tkinter import *
import mysql.connector

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_11_30"
        )
print(create_conn())

def insert_data():
    print("Insert button clicked")

def search_data():
    print("Search button clicked")
    

root=Tk()
root.title("My Tkinter Window")
root.geometry("320x370")
root.resizable(width=1,height=1)

x=Label(root,text="ID")
x.place(x=50,y=50)

y=Label(root,text="Fname")
y.place(x=50,y=100)

z=Label(root,text="Last Name")
z.place(x=50,y=150)

x=Entry(root)
x.place(x=150,y=50)

y=Entry(root)
y.place(x=150,y=100)

z=Entry(root)
z.place(x=150,y=150)


x=Button(root,text="INSERT",bg="BLACK",fg="white",font=("timesnewroman",12),command=insert_data)
x.place(x=10,y=300)

y=Button(root,text="SEARCH",bg="black",fg="white",font=("timesnewroman",12),command=search_data)
y.place(x=85,y=300)


