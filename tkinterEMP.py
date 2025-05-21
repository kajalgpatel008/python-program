from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_11_30"
        )

def insert_data():
     if  e_ename.get()=="" or e_job.get()=="" or e_mgr.get()=="" or e_sal.get()=="" or e_deptno.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
     else: 
        conn=create_conn()
        cursor=conn.cursor()  
        query="insert into emp(ename,job,mgr,sal,deptno) values(%s,%s,%s,%s,%s)"
        args=(e_ename.get(),e_job.get(),e_mgr.get(),e_sal.get(),e_deptno.get())
        cursor.execute(query,args)
        conn.commit()
        e_ename.delete(0,'end')
        e_job.delete(0,'end')
        e_mgr.delete(0,'end')
        e_sal.delete(0,'end')
        e_deptno.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")
        conn.close()        
def search_data():
        e_ename.delete(0,'end')
        e_job.delete(0,'end')
        e_mgr.delete(0,'end')
        e_sal.delete(0,'end')
        e_deptno.delete(0,'end')
        if e_empno.get()=="":   
            msg.showinfo("Search Status","empno Is Mandatory")
        else:
           conn=create_conn()
           cursor=conn.cursor()
           query="select * from emp where empno=%s "
           args=(e_empno.get(),)
           cursor.execute(query,args)
           row=cursor.fetchall()
           if row:
               e_ename.insert(0,row[0][1])
               e_job.insert(0,row[0][2])
               e_mgr.insert(0,row[0][3])
               e_sal.insert(0,row[0][4])
               e_deptno.insert(0,row[0][5])
           else:
              msg.showinfo("Search Status","empno Not Found")
           conn.close()  

def update_data():
       if e_empno.get()=="" or e_ename.get()=="" or e_job.get()=="" or e_mgr.get()=="" or e_sal.get()=="" or e_deptno.get()=="":
        msg.showinfo("update Status","All Fields Are Mandatory")
       else: 
         conn=create_conn()
         cursor=conn.cursor()  
         query="update emp set deptno=%s,ename=%s,job=%s,mgr=%s,sal=%s where empno=%s "
         args=(e_deptno.get(),e_ename.get(),e_job.get(),e_mgr.get(),e_sal.get(),e_empno.get())
         cursor.execute(query,args)
         conn.commit()
         e_ename.delete(0,'end')
         e_job.delete(0,'end')
         e_mgr.delete(0,'end')
         e_sal.delete(0,'end')
         e_deptno.delete(0,'end')
         msg.showinfo("update Status","Data updated Successfully")
             
    
def delete_data():
     if e_empno.get()=="": 
            msg.showinfo("Delete Status","empno Is Mandatory")
     else:
         conn=create_conn()
         cursor=conn.cursor()
         query="delete from emp where empno=%s "
         args=(e_empno.get(),)
         cursor.execute(query,args)
         conn.commit()
         e_ename.delete(0,'end')
         e_job.delete(0,'end')
         e_mgr.delete(0,'end')
         e_sal.delete(0,'end')
         e_deptno.delete(0,'end')
         msg.showinfo("Delete Status","Data Deleted Successfully")
root=Tk()
root.title("Tkinter Emp example")
root.geometry("320x370")

l_empno=Label(root,text="empno")
l_empno.place(x=50,y=50)

l_ename=Label(root,text="ename")
l_ename.place(x=50,y=100)

l_job=Label(root,text="job")
l_job.place(x=50,y=150)

l_mgr=Label(root,text="mgr")
l_mgr.place(x=50,y=200)

l_sal=Label(root,text="sal")
l_sal.place(x=50,y=250)

l_deptno=Label(root,text="deptno")
l_deptno.place(x=50,y=300)

e_empno=Entry(root)
e_empno.place(x=150,y=50)

e_ename=Entry(root)
e_ename.place(x=150,y=100)

e_job=Entry(root)
e_job.place(x=150,y=150)

e_mgr=Entry(root)
e_mgr.place(x=150,y=200)

e_sal=Entry(root)
e_sal.place(x=150,y=250)

e_deptno=Entry(root)
e_deptno.place(x=150,y=300)


x=Button(root,text="INSERT",bg="black",fg="white",command=insert_data)
x.place(x=10,y=350)

x=Button(root,text="SEARCH",bg="black",fg="white",command=search_data)
x.place(x=90,y=350)

x=Button(root,text="UPDATE",bg="black",fg="white",command=update_data)
x.place(x=170,y=350)

x=Button(root,text="DELETE",bg="black",fg="white",command=delete_data)
x.place(x=250,y=350)

