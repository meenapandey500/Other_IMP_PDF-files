#create  todotable
import pymysql
class todo:
    def __init__(self):
        __servername="localhost"
        __username="root"
        __password=""
        __dbname="todo1"
        try:
            self.con=pymysql.connect(__servername,__username,__password,__dbname)
        except Exception:
            print("Connection Error")
        else:
            print("connection successfully")
    def __del__(self):
        self.con.close()

    def createtable(self):
        query="CREATE TABLE todo2(id int primary key,title varchar(255) not null,bodytext varchar(200),status tinyint not null)"
        cur=self.con.cursor()
        try:
            cur.execute(query)            
        except Exception:
            print("Table error")
        else:
            print("create table suucessfully")
    def insertrecord(self):
        id=int(input("Enter id=>"))
        
        query="INSERT INTO todo(id,title,bodytext,statustiny)VALUES(%s,'introduction to python','python is a highly interpreted lang.',0)"
        cur=self.con.cursor()
        try:
            cur.execute(query,id)
        except Exception:
            print("Query  error")
        else:
            self.con.commit()#save database
        print("save record successfully")
        cur.close()
    def menu(self):
        print("1 Create Table \n 2insertrecord\n3.Exit")
#call function
t1=todo()
while True:
    t1.menu()
    ch=int(input("enter your choice=>"))
    if ch==1:
        t1.createtable()
    elif ch==2:
        t1.insertrecord()
    elif ch==3:
        break
        
del t1   
    
    
        
        
        
        
