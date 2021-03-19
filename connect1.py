#Create connectivity with python and mysqlserver
import pymysql
class College:  #College user defined class name
    def __init__(self): #constructor function
        self.__servername="localhost"  #private variable
        self.__username="root"
        self.__password=""
        self.__dbname="college"  #dbname means databasename
        try:
            self.con=pymysql.connect(self.__servername,self.username,self.password,self.__dbname)
            #con user defined connection name
            print("Connect successfully")
        except:
            print("connectivity not work")
    def __del__(self): #destrcutor function 
        self.con.close()
        print("Connection close")
