#create connectivity with python and mysqlserver
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
