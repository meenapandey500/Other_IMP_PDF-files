import tkinter as tk
import pymysql
import os
import sys
def login():
    conn=pymysql.connect(host="localhost",user="root",password="",database="employee_management")
    cur=conn.cursor()
    u=euid.get()
    p=epass.get()
    q="select * from login where userid='" + u + "' and password='" + p + "'"
    cur.execute(q)
    records=cur.fetchall()
    for row in records:
        os.system('python mainpage.py')
        break
    else:
        print("no data found")
    conn.close()
window=tk.Tk()
window.title("Login form")
window.geometry("500x300")
luid=tk.Label(window,text="User Id :")
luid.place(x=100,y=50)
euid=tk.Entry(window)
euid.place(x=200,y=50)
lpass=tk.Label(window,text="Password :")
lpass.place(x=100,y=80)
epass=tk.Entry(window,show="*")
epass.place(x=200,y=80)
lb=tk.Button(window,text="Login",command=login)
lb.place(x=220,y=120)
window.mainloop()
