class hotel:
    def menu(self):
        print("\n 1. User Record \n 2. Employee Record \n 3. Exit" )
    
    def menu2(self):
        print("\n 1. Insert User Record \n 2. Show User Record \n 3. Delete User Record \n 4. Exit" )
    
    def menu3(self):
        print("\n 1. Insert Empolyee Record \n 2. Show Empolyee Record \n 3. Update Employee Salary \n 4.Update Employee Department \n 5. Delete Employee \n 6. Exit" )
    
    def __init__(self):
        import pymysql
        #to create a connection string (between python and mysqlserver)
        
        self.servername="localhost"
        self.username="root"
        self.password=""
        self.dbname="hotel_management"
        try:
            self.con=pymysql.connect(self.servername,self.username,self.password,self.dbname)
        except:
            print("Connectivity Error")
        else:
            print("Connect successfully")
    def insert_record(self):
        #insert record
        self.e=int(input("Enter register no. : "))
        self.n=input("Enter user Name ")  #varchar type in table=string
        self.g=(input("Enter user gender : "))
        self.a=int(input("Enter user age :"))
        self.c=input("Enter user city :")
        self.ad=input("Enter user address :")
        self.id=int(input("Enter user pan/adhar id :"))
        self.pe=int(input("Enter how many people saty :"))
        self.s=int(input("Enter many days stay :"))

        #to insert data from front end (python's output screen) to backend(sqlserver)
        #the fire SQL Query
        
        query="INSERT INTO USER(enroll,name,gender,age,city,add,id,people,stay)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"  #%s means string
        val=(self.e,self.n,self.g,self.a,self.c,self.ad,self.id,self.pe,self.s) #val tuple variable
                       #prepared cursor
        cur=self.con.cursor()
                       #run insert query
        try:
            cur.execute(query,val)
        except:
            print("Query Error")
        else:
        #save in database  use commit()
            self.con.commit()
            print("Record Insert Successfully")
        #close connection
        cur.close()
    
   
    def show_record(self):
                    #Fire Select Query
        query="SELECT * FROM USER"
                    #prepared cursor
        cur=self.con.cursor()
                    #run select query
        cur.execute(query)
        result=cur.fetchall()  #fetchone() to display only first record
        print(result)
        self.con.close()
     
    def delete(self):
        self.e=int(input("Enter register no. to be deleted : "))
        #Fire delete Query
        query="delete FROM USER WHERE enroll=%s"
        #prepared cursor
        cur=self.con.cursor()
        #run delete query
        try:
            cur.execute(query,self.e)
            self.con.commit() #to changes permanently in table
            print("Delete Record successfully")
        except:
            print("Record not found")
        cur.close()
    
    def insert_record_e(self):
        #insert record
        self.id=int(input("Enter Employee Id : "))
        self.n=input("Enter Employee Name ")  #varchar type in table=string
        self.a=int(input("Enter Employee Age : "))
        self.d=input("Enter Employee Department :")
        self.s=int(input("Enter Employee Salary :"))


        #to insert data from front end (python's output screen) to backend(sqlserver)
        #the fire SQL Query
        
        query="INSERT INTO EMPLOYEE(id,name,age,department,salary)values(%s,%s,%s,%s,%s)"  #%s means string
        val=(self.id,self.n,self.a,self.d,self.s) #val tuple variable
                       #prepared cursor
        cur=self.con.cursor()
                       #run insert query
        try:
            cur.execute(query,val)
        except:
            print("Query Error")
        else:
        #save in database  use commit()
            self.con.commit()
            print("Record Insert Successfully")
        #close connection
        cur.close()
        
    def show_record_e(self):
                    #Fire Select Query
        query="SELECT * FROM EMPLOYEE"
                    #prepared cursor
        cur=self.con.cursor()
                    #run select query
        cur.execute(query)
        result=cur.fetchall()  #fetchone() to display only first record
        print(result)
        self.con.close()
        
    def update_salary(self):
        self.id=int(input("Enter employee id no. to be updated : "))
        self.s=int(input("Enter new salary : "))
        #Fire delete Query
        query="UPDATE EMPLOYEE SET SALARY=%s WHERE id=%s"
        #prepared cursor
        cur=self.con.cursor() #to keep cursor on particular path
        val=(self.id,self.s)
        #run update query
        try:
            cur.execute(query,val)
            self.con.commit() #to changes permanently in table
            print(" Record Update  successfully")
        except:
            print("Record not found")
        cur.close()
            
    def update_department(self):
        self.id=int(input("Enter employee id no. to be updated : "))
        self.d=input("Enter new Department : ")
        #Fire delete Query
        query="UPDATE EMPLOYEE SET DEPARTMENT=%s WHERE id=%s"
        #prepared cursor
        cur=self.con.cursor() #to keep cursor on particular path
        val=(self.d,self.id)
        #run update query
        try:
            cur.execute(query,val)
            self.con.commit() #to changes permanently in table
            print(" Record Update  successfully")
        except:
            print("Record not found")
        cur.close() 
        

    def delete_e(self):
        self.id=int(input("Enter Employee Id no. to be deleted : "))
        #Fire delete Query
        query="delete FROM EMPOYEE WHERE id=%s"
        #prepared cursor
        cur=self.con.cursor()
        #run delete query
        try:
            cur.execute(query,self.id)
            self.con.commit() #to changes permanently in table
            print("Delete Record successfully")
        except:
            print("Record not found")
        cur.close()
    

        
        
        
#main program
h=hotel()
while(True):
    h.menu()
    ch=int(input("Enter your choice :"))
    if(ch==1):
        h.menu2()
        while(True):
            ch=int(input("Enter your choice"))
            if(ch==1):
                h.insert_record()
            elif(ch==2):
                h.show_record()
            elif(ch==3):
                h.delete()
            elif(ch==4):
                break
            else:
                print("Invalid Choice")
    elif(ch==2):
        h.menu3()
        while(True):
            if(ch==1):
                h.insert_record_e()
            elif(ch==2):
                h.show_record_e()
            elif(ch==3):
                h.update_salary()
            elif(ch==4):
                h.update_department()
            elif(ch==5):
                h.delete_e()
            elif(ch==6):
                break
            else:
                print("Invalid Choice ")
    elif(ch==3):
        break
    else:
        print("Invalid choice ")
