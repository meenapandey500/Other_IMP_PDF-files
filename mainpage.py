import pymysql
import menu as m
class studentrecord:
      def __init__(self):
            self.__servername="localhost"
            self.__username="root"
            self.__password=""
            self.__dbname="ITVedantProject"
            try:
                  self.con=pymysql.connect(self.__servername,self.__username,self.__password,self.__dbname)
                  print("")
            except:
                  print("Connection Error")
      def admin(self):
            print("\t\t ********** Student Record Keeping System Databse ********** ")
            print("")
            print("\t\t **********   Created By Nitesh Raghunath Kuware   ********** ")
            print("")
            print("\t\t           -------------------------    ADMIN  LOGIN    ------------------------ ")
            while(True):
                  try:
                        print("")
                        self.uname=input("\t\t\tUsername : ")
                        self.passwd=input("\t\t\tPassword : ")
                        if(self.uname=="Admin") & (self.passwd=="jdc@"):
                              print("\t\t\t================================")
                              print("\t\t\t\tLogin Successful")
                              break
                        raise ValueError
                  except ValueError:
                        print("\t\t\tRe - enter Username & Password ")
            print("\t\t\t================================")
            print("\t\t\t1.  Enter 1 for Admission \n\t\t\t2. Enter 2 for Delete Record\n\t\t\t3. Enter 3 for Update Record\n\t\t\t4. Enter 4 for View Record\n\t\t\t5. Enter 5 for View FYJC Data\n\t\t\t6. Enter 6 for View SYJC Data\n\t\t\t7. Enter 7 for Fee Details\n\t\t\t8. Enter 8 for Single Fee Record\n\t\t\t9. Enter 9 for Payment\n\t\t\t10. Enter 10 for Logout")
            print("")
            while(True):
                  print("\t\t\t===========================")
                  ch=int(input("\t\t\tEnter your choice   : "))
                  print("\t\t\t===========================")
                  if(ch==1):
                        m.admission.add(self)
                  elif(ch==2):
                        m.admission.delete(self)
                  elif(ch==3):
                        m.admission.update(self)
                  elif(ch==4):
                        m.admission.show(self)
                  elif(ch==5):
                        m.admission.fyshow(self)
                  elif(ch==6):
                        m.admission.syshow(self)
                  elif(ch==7):
                        m.admission.feedetail(self)
                  elif(ch==8):
                        m.admission.sfee(self)
                  elif(ch==9):
                        m.admission.pay(self)
                  elif(ch==10):
                        print("\t\t\t         You Logout Successfully !")
                        break
                  else:
                        print("\t\t\tInvalid Choice ")
      def __del__(self):
            self.con.close()
      
      

