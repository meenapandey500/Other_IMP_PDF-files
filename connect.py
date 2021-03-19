#Create connectivity with python and mysqlserver
import pymysql
class College:  #College user defined class name
    def __init__(self): #constructor function
        self.__servername="localhost"  #private variable
        self.__username="root"
        self.__password=""
        self.__dbname="college1"  #dbname means databasename
        try:
            self.con=pymysql.connect(self._servername,self.username,self.password,self._dbname)
            #con user defined connection name
            print("Connect successfully")
        except:
            print("connectivity not work")
    def __del__(self): #destrcutor function 
        self.con.close()
        print("Connection close")
