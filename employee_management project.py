import mysql.connector as a
con=a.connect(host="localhost",user="root",password="",database="employee_management")
def npersonal():
    n=input("Enter Employee Name: ")
    c=input("Enter Employee city name: ")
    d=input("Enter Employee Date of birth: ")
    p=input("Enter Employee phone: ")
    data=(n,c,d,p)
    sql="insert into personal values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def personal():
    sql="select * from personal"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()

def noffice():
    ec=input("Enter Employee code: ")
    n=input("Enter Employee name: ")
    ps=input("Enter Employee post: ")
    j=input("Enter Employee joining date: ")
    bp=int(input("Enter assigned salary: "))
    data=(ec,n,ps,j,bp)
    sql="insert into office values(%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered successfully")
    main()
def office():
    sql="select * from office"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()
def nsalary():
    ec=input("Enter Employee code: ")
    v=(ec,)
    sql="select BasicPay from office where Ecode=%s"
    c=con.cursor()
    c.execute(sql,v)
    bs=c.fetchone()
    n=input("Enter Employee name: ")
    y=input("Enter year: ")
    m=input("Enter month: ")
    wd=int(input("Enter working days: "))
    td=int(input("Enter total days : "))
    fp=bs[0]/td*wd
    data=(ec,n,y,m,wd,fp)
    sql="insert into salary values(%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered successfully")
    main()
def salary():
    sql="select * from salary"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()
def main():
    print(""""
          1.Add new employee personal details
          2.Display employees personal details
          3.Add new employee office details
          4.Display employee office details
          5.Enter salary details of employee
          6.Display salary details of employee"""")
    choice=input("Enter task no: ")
    while True:
        if(choice=='1'):
            npersonal()
        elif(choice=='2'):
            personal()
        elif(choice=='3'):
            noffice()
        elif(choice=='4'):
            office()
        elif(choice=='5'):
            nsalary()
        elif(choice=='6'):
            salary()
        else:
            print("Wrong choice...")
main()
