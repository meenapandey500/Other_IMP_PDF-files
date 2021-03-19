class emoplyee:
    def menu(self):
        print("\n 1. Insert Record \n 2. Show Record \n 3. Update Employee Salary \n 4.Update Employee Department \n 5. Delete Employee \n 6. Exit" )
        

    def __init__(self):
        import pymysql
        #to create a connection string (between python and mysqlserver)
        
        self.servername="localhost"
        self.username="root"
        self.password=""
        self.dbname="employeemanagement"
        try:
            self.con=pymysql.connect(self.servername,self.username,self.password,self.dbname)
        except:
            print("Connectivity Error")
        else:
            print("Connect successfully")
            
    def insert_record(self):
        #insert record
        self.id=int(input("Enter Employee Id no. : "))
        self.n=input("Enter Employee Name ")  #varchar type in table=string
        self.d=(input("Enter Employee Department : "))
        self.s=int(input("Enter Employee Salary :"))

        #to insert data from front end (python's output screen) to backend(sqlserver)
        #the fire SQL Query
        
        query="INSERT INTO EMPLOYEE_MANAGEMENT(id,name,department,salary)values(%s,%s,%s,%s)"  #%s means string
        val=(self.id,self.n,self.d,self.s) #val tuple variable
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
        query="SELECT * FROM EMPLOYEE_MANAGEMENT"
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
        query="UPDATE EMPLOYEE_MANAGEMENT SET SALARY=%s WHERE id=%s"
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
        query="UPDATE EMPLOYEE_MANAGEMENT SET DEPARTMENT=%s WHERE id=%s"
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
        
    def delete(self):
        self.id=int(input("Enter Employee id no. to be deleted : "))
        #Fire delete Query
        query="delete FROM EMPLOYEE_MANAGEMENT WHERE id=%s"
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
em=emoplyee()
while(True):
    em.menu()
    ch=int(input("Enter your choice :"))
    if(ch==1):
        em.insert_record()
    elif(ch==2):
        em.show_record()
    elif(ch==3):
        em.update_salary()
    elif(ch==4):
        em.update_department()
    elif(ch==5):
        em.delete()
    elif(ch==6):
        break
    else:
        print("Invalid choice ")

