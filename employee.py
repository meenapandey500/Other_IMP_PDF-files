#Create connectivity with python and mysqlserver
import pymysql
class  Employee: #Company user defined class name
    def __init__(self): #constructor function
       self.__servername="localhost"#private variable
       self.__username="root"
       self.__password=""  
       self.__dbname="employee" #dbname means databasename
       try:
           self.con=pymysql.connect(self.__servername,self.__username,self.__password,self.__dbname)
           #con user defined connection name
           print("Connect successfully")
       except:
           print("Connectivity not work")
    def __del__ (self): #destructor function
          self.con.close()
          print("Connection close")
    def insertrecord(self):
         Id=int(input("Enter Employee Id :"))
         Name=input("Enter Employee Name")
         Department=input("Enter Employee Department :")
         Salary=int(input("Enter Employee Salary :"))
         q1="INSERT INTO Employee(Id,Name,Department,Salary)values(%s,%s,%s,%s)"
         val=(Id,Name,Department,Salary)
         #Creating Cursor
         cursor=self.con.cursor() #cursor() inbuilt function
         #Execute(run) the Query
         cursor.execute(q1,val)
         #Commit changes in the database.
         self.con.commit()
         print("Record save successfully")

#main program
emp=Employee()
emp.insertrecord()
del emp
         
