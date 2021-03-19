import tkinter as tk
import pymysql
import tkinter.messagebox as mb
import os
def adddata():
    conn=pymysql.connect(host="localhost",user="root",password="",database="employee_management")
    cur=conn.cursor()
    q="insert into employee(eid,ename,egender,ecity,edesig,esalary)values("+eid.get()+",'"+en.get()+"','"+gender.get()+"','"+ec.get()+"','"+ed.get()+"',"+es.get()+")"
    cur.execute(q)
    conn.commit()

    eid.delete(0,'end')
    en.delete(0,'end')
    ec.delete(0,'end')
    ed.delete(0,'end')
    es.delete(0,'end')

    eid.focus()

    mb.showinfo("",str(cur.rowcount)+"Record inserted successfully")
    conn.close()

def searchdata():
    conn=pymysql.connect(host="localhost",user="root",password="",database="employee_management")
    cur=conn.cursor()
    q="select * from employee where eid="+eid.get()+""
    cur.execute(q)
    records=cur.fetchall()

    list1.delete(0,'end')

    for row in records:
        d=str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5])
        n.set(str(row[1]))
        c.set(str(row[3]))
        deg.set(str(row[4]))
        s.set(str(row[5]))
    list1.insert(list1.size()+1,d)
    conn.close()   

def showdata():
    conn=pymysql.connect(host="localhost",user="root",password="",database="employee_management")
    cur=conn.cursor()
    q="select * from employee"
    cur.execute(q)
    records=cur.fetchall()

    list1.delete(0,'end')

    for row in records:
        d=str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5])
        list1.insert(list1.size()+1,d)
    conn.close()
    
def updatedata():
    conn=pymysql.connect(host="localhost",user="root",password="",database="employee_management")
    cur=conn.cursor()
    q="update employee set ename='"+en.get()+"',egender='"+gender.get()+"',ecity='"+ec.get()+"',edesig='"+ed.get()+"',esalary="+es.get()+" where eid="+eid.get()+""
    cur.execute(q)
    conn.commit()
    list1.delete(0,'end')
    eid.delete(0,'end')
    en.delete(0,'end')
    ec.delete(0,'end')
    ed.delete(0,'end')
    es.delete(0,'end')
    mb.showinfo("",str(cur.rowcount)+" Record Update Successfully")
    eid.focus()

    conn.close()


def deletedata():
    conn=pymysql.connect(host="localhost",user="root",password="",database="employee_management")
    cur=conn.cursor()
    q="delete from employee where eid="+eid.get()+""
    cur.execute(q)
    conn.commit()
    mb.showinfo("",str(cur.rowcount)+"Record successfully deleted")
    conn.close()
def cleardata():
    list1.delete(0,'end')
    eid.delete(0,'end')
    en.delete(0,'end')
    ec.delete(0,'end')
    ed.delete(0,'end')
    es.delete(0,'end')
def next():
    os.system('python salary.py')
    
window=tk.Tk()
window.title("Employee Management System")
window.geometry("700x700")
window.configure(bg="cyan2")
empid=tk.Label(window,text="Employee ID",fg="white",bg="orangered2",font=("Arial",12))
empid.place(x=10,y=25)
eid=tk.Entry(window,width="25",font=("Arial",10))
eid.place(x=150,y=25)
n=tk.StringVar()
c=tk.StringVar()
deg=tk.StringVar()
s=tk.StringVar()
ename=tk.Label(window,text="Employee Name",fg="white",bg="orangered2",font=("Arial",12))
ename.place(x=10,y=67)
en=tk.Entry(window,width="25",font=("Arial",10),textvariable=n)
en.place(x=150,y=65)
empg=tk.Label(window,text="Gender",fg="white",bg="orangered2",font=("Arial",12))
empg.place(x=10,y=110)
gender=tk.StringVar()
male=tk.Radiobutton(window,text="Male",value="M",bg="cyan2",variable=gender)
male.place(x=150,y=110)
female=tk.Radiobutton(window,text="Female",value="F",bg="cyan2",variable=gender)
female.place(x=210,y=110)
empc=tk.Label(window,text="Employee City",fg="white",bg="orangered2",font=("Arial",12))
empc.place(x=10,y=155)
ec=tk.Entry(window,width="25",font=("Arial",10),textvariable=c)
ec.place(x=150,y=155)
empd=tk.Label(window,text="Employee Designation",fg="white",bg="orangered2",font=("Arial",12))
empd.place(x=10,y=200)
ed=tk.Entry(window,width="25",font=("Arial",10),textvariable=deg)
ed.place(x=210,y=200)
emps=tk.Label(window,text="Employee Salary",fg="white",bg="orangered2",font=("Arial",12))
emps.place(x=10,y=245)
es=tk.Entry(window,width="25",font=("Arial",10),textvariable=s)
es.place(x=180,y=245)
ademp=tk.Button(window,text="Add Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=adddata)
ademp.place(x=93,y=500)
sremp=tk.Button(window,text="Search Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=searchdata)
sremp.place(x=210,y=500)
shemp=tk.Button(window,text="Show All Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=showdata)
shemp.place(x=347,y=500)
uemp=tk.Button(window,text="Update Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=updatedata)
uemp.place(x=495,y=500)
demp=tk.Button(window,text="Delete Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=deletedata)
demp.place(x=629,y=500)
clr=tk.Button(window,text="Clear All Text",fg="white",bg="forestgreen",font=("Arial",12),command=cleardata)
clr.place(x=750,y=500)
sal=tk.Button(window,text="Salary Compute",fg="white",bg="forestgreen",font=("Arial",12),command=next)
sal.place(x=880,y=500)
list1=tk.Listbox(width='100',height='22')
list1.place(x=500,y=25)
window.mainloop()
