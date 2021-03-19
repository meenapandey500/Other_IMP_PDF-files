import pymysql
import tkinter.messagebox as mb
from tkinter import *
def searchdata():
    conn = pymysql.connect(host='localhost',user='root',password='',database='employee_database')

    cur = conn.cursor()
        
    q = "select * from employee where eid="+eid.get()+"
    
    cur.execute(q)
    records = cur.fetchall()

    list1.delete(0,'end')
    
    for row in records:
        d=str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])
        list1.insert(list1.size()+1,d)
    
    conn.close()
def insertdata():    
    connection = pymysql.connect(host='localhost',user='root',password='',database='employee_database')

    cur = connection.cursor()

    q = "insert into employee(ID, NAME, DEPARTMENT, SALARY) values("+rID.get()+",'"+rname.get()+"','"+rdept.get()+"',
    "+rsalary.get()+")"
    
    cur.execute(q)
    connection.commit()

    rID.delete(0,'end')
    rname.delete(0,'end')
    rdept.delete(0,'end')
    rsalary.delete(0,'end')

    rID.focus()
    
    mb.showinfo("",str(cur.rowcount)+" Record Inserted Successfully")
    
    connection.close()
    
def showdata():
    connection = pymysql.connect(host='localhost',user='root',password='',database='employee_database')

    cur = connection.cursor()
        
    sql_query = "select * from employee"
    
    cur.execute(sql_query)
    records = cur.fetchall()

    list1.delete(0,'end')
    
    for row in records:
        d=str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])
        list1.insert(list1.size()+1,d)
    
    connection.close()



def updatedata():
    connection = pymysql.connect(host='localhost',user='root',password='',database='employee_database')

    db_cursor = connection.cursor()
        
    sql_query = "update employee set Name = '"+rname.get()+"',Department = '"+rdept.get()+"',Salary = "+rsalary.get()+" where ID ="+rID.get()+""
    
    db_cursor.execute(sql_query)
    connection.commit()

    rID.delete(0,'end')
    rname.delete(0,'end')
    rdept.delete(0,'end')
    rsalary.delete(0,'end')

    rID.focus()
    
    connection.close()
    
def deletedata():
    connection = pymysql.connect(host='localhost',user='root',password='',database='employee_database')

    db_cursor = connection.cursor()
        
    sql_query = "delete from employee where ID ="+rID.get()+""
    
    db_cursor.execute(sql_query)
    connection.commit()
    mb.showinfo("",str(db_cursor.rowcount)+" Record Deleted Successfully")


root = Tk()
root.title("Employement Details")
root.geometry("700x500")



ID = Label(root,text="ID Of Employee:")
ID.place(x=10,y=10)

name = Label(root,text="Name Of Employee:")
name.place(x=10,y=50)

dept = Label(root,text="Department Of Employee:")
dept.place(x=10,y=100)

salary = Label(root,text="Salary Of Employee:")
salary.place(x=10,y=150)


rID = Entry(root,text="")
rID.place(x=150,y=10)

rname = Entry(root,text="")
rname.place(x=150,y=50)

rdept = Entry(root,text="")
rdept.place(x=150,y=100)

rsalary = Entry(root,text="")
rsalary.place(x=150,y=150)


button1=Button(root,text="Save",command=insertdata)
button1.place(x=20,y=200)

button2=Button(root,text="Show Data",command=showdata)
button2.place(x=70,y=200)

button4=Button(root,text="Update",command=updatedata)
button4.place(x=150,y=200)

button5=Button(root,text="Delete",command=deletedata)
button5.place(x=210,y=200)


list1 = Listbox(root,width='50')
list1.place(x=300,y=20)

root.mainloop()









