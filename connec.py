#create connectivity with python and mysqlserver
import pymysql
class college: #college user defined class name
    def__init__(self): #constructor function
       self.__serevername="localhost"#private variable
       self.__username="root"
       self.__password=""  
       self.__dbname="college" #dbname means databasename
       try:
           self.con=pymysql.connect(self.__servername,self.__username,self.__password,self.__dbname)
           #con user defined connection name
           print("connect successfully")
       except:
           print("connectivity not work")
    def__del__(self): #destructor function
          self.con.close()
          print("Connection close")
          
