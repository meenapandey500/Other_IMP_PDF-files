import pymysql
class admission:
      def __init__(self):
            self.__servername="localhost"
            self.__username="root"
            self.__password=""
            self.__dbname="ITVedantProject"
            try:
                  self.con=pymysql.connect(self.__servername,self.__username,self.__password,self.__dbname)
                  print("")
            except:
                  print("\t\t\tConnection Error")
      def add(self):
            self.id=int(input("\t\t\tEnter Student' ID   : "))
            self.roll=int(input("\t\t\tEnter Student's ROLL NO.   : "))
            self.name=input("\t\t\tEnter Student's NAME   : ")
            self.std=input("\t\t\tEnter Student's CLASS (FY/SY) : ")
            self.addr=input("\t\t\tEnter Student's ADDRESS : ")
            self.pincode=int(input("\t\t\tEnter PINCODE : "))
            self.ph=int(input("\t\t\tEnter Student's CONTACT : "))
            self.fph=int(input("\t\t\tEnter Father's CONTACT : "))
            self.tot=72000
            print("\t\t\tTotal Fees : ",self.tot)
            self.paidfee=int(input("\t\t\tCurrent Paid Fees : "))
            self.pendfee=self.tot-self.paidfee
            print("\t\t\tPending Fees : ",self.pendfee)
            query="INSERT INTO studentadm values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(self.id,self.roll,self.name,self.std,self.addr,self.pincode,self.ph,self.fph,self.tot,self.paidfee,self.pendfee)
            cur=self.con.cursor()
            try:
                  cur.execute(query,val)
            except:
                  print("\t\t\tERROR IN QUERY ")
            else:
                  self.con.commit()
                  print("\t\t\tRecord Insert Successfully ")
                  print("")
      def delete(self):
            self.id=int(input("\t\t\tEnter Student's ID to DELETE  : "))
            query="DELETE FROM studentadm WHERE ID=%s"
            cur=self.con.cursor()
            try:
                  cur.execute(query,self.id)
            except:
                  print("\t\t\tRecord Not Found ")
            else:
                  self.con.commit()
                  print("\t\t\tRecord Deleted Successfully ")
                  print("\t\t\t")
      def update(self):
            self.id=int(input ("\t\t\tEnter Student's ID for UPDATE  : "))
            print("\t\t\t1. Enter 1 for Update Roll Number \n\t\t\t2. Enter 2 for Update Name\n\t\t\t3. Enter 3 for Update Class \n\t\t\t4. Enter 4 for Update Address \n\t\t\t 5. Enter 5 for Update Contact\n\t\t\t6. Enter 6 for Update Father's Contact\n\t\t\t7.Enter 7 for Exit ")
            while(True):
                  print("\t\t\t=====================================")
                  ch=int(input("\t\t\tEnter your Choice for Updation   : "))
                  print("\t\t\t=====================================")
                  if(ch==1):
                        self.roll=int(input("\t\t\tEnter New Roll Number          :"))
                        query="update studentadm set ROLLNO=%s where ID=%s"
                        cur=self.con.cursor()
                        val=(self.roll,self.id)
                        try:
                              cur.execute(query,val)
                              self.con.commit()
                              print("\t\t\t -- New Roll Number is Updated -- ")
                        except:
                              print("\t\t\t Oops ,Record Not Found !")
                  if(ch==2):
                        self.name=input("\t\t\tEnter New Student's Name      : ")
                        query="update studentadm set NAME=%s where ID=%s"
                        cur=self.con.cursor()
                        val=(self.name,self.id)
                        try:
                              cur.execute(query,val)
                              self.con.commit()
                              print(" \t\t\t-- New Name  is Updated --")                              
                        except:
                              print(" \t\t\tOops ,Record Not Found !")
                  if(ch==3):
                        self.cls=input("\t\t\tEnter New Student's Class  : ")
                        query="update studentadm set STD=%s where ID=%s"
                        cur=self.con.cursor()
                        val=(self.cls,self.id)
                        try:
                              cur.execute(query,val)
                              self.con.commit()
                              print(" \t\t\t-- New Class  is Updated --")
                        except:
                              print("\t\t\t Oops ,Record Not Found !")
                  if(ch==4):
                        self.adr=input("\t\t\tEnter New Student's Address  : ")
                        query="update studentadm set ADDR=%s where ID=%s"
                        cur=self.con.cursor()
                        val=(self.adr,self.id)
                        try:
                              cur.execute(query,val)
                              self.con.commit()
                              print("\t\t\t     -- New Address  is Updated -- ")
                        except:
                              print("\t\t\t Oops ,Record Not Found !")
                  if(ch==5):
                        self.ph=int(input("\t\t\tEnter New Student's Contact  : "))
                        query="update studentadm set PHONE=%s where ID=%s"
                        cur=self.con.cursor()
                        val=(self.ph,self.id)
                        try:
                              cur.execute(query,val)
                              self.con.commit()
                              print("\t\t\t     -- New Contact  is Updated -- ")
                        except:
                              print("\t\t\t Oops ,Record Not Found !")
                  if(ch==6):
                        self.fph=int(input("\t\t\tEnter New Father's Contact  : "))
                        query="update studentadm set FPHONE=%s where ID=%s"
                        cur=self.con.cursor()
                        val=(self.fph,self.id)
                        try:
                              cur.execute(query,val)
                              self.con.commit()
                              print("\t\t\t     -- New Contact  is Updated -- ")
                        except:
                              print("\t\t\t Oops ,Record Not Found !")
                  if(ch==7):
                        print("\t\t\t           -- All Updation Done -- ")
                        break
      def show(self):
            query="SELECT * FROM studentadm"
            try:
                  cur=self.con.cursor()
                  cur.execute(query)
            except:
                  print("\t\t\tError in Query ")
            else:
                  result=cur.fetchall()
                  for row in result:
                        print("\t\t\t",row)
      def fyshow(self):
            query="SELECT * FROM studentadm WHERE STD='FY' "
            try:
                  cur=self.con.cursor()
                  cur.execute(query)
            except:
                  print("\t\t\tError in Query ")
            else:
                  result=cur.fetchall()
                  for row in result:
                        print("\t\t\t",row)
      def syshow(self):
            query="SELECT * FROM studentadm WHERE STD='SY'"
            try:
                  cur=self.con.cursor()
                  cur.execute(query)
            except:
                  print("\t\t\tError in Query ")
            else:
                  result=cur.fetchall()
                  for row in result:
                        print("\t\t\t",row)
      def feedetail(self):
            print("\t\t\tPending Fees ")
            query="select ID,NAME,PEEE from studentadm"
            try:
                  cur=self.con.cursor()
                  cur.execute(query)
            except:
                  print("\t\t\tError in Query ")
            else:
                  result=cur.fetchall()
                  for row in result:
                        print("\t\t\t",row)
      def sfee(self):
            self.id=int(input("\t\t\tEnter ID of Student to see Single Record of Fees : "))
            query="select ID,NAME,STD,PEEE from studentadm where ID=%s"
            try:
                  cur=self.con.cursor()
                  cur.execute(query,self.id)
            except:
                  print("\t\t\t Oops ,Record Not Found !")
            else:
                  result=cur.fetchall()
                  print("\t\t\t",result)
      def pay(self):
            self.id=int(input("\t\t\tEnter ID for Payment of Fees :"))
            print("\t\t\tTotal Fees are : 72000 ")
            self.p=int(input("\t\t\t Enter Amount for Payment : "))
            self.bal=72000 - self.p
            print("\t\t\tPending Fees are : ",self.bal)
            query="update studentadm set PEEE=%s where ID=%s"
            cur=self.con.cursor()
            val=(self.bal,self.id)
            try:
                  cur.execute(query,val)
                  self.con.commit()
                  print("\t\t\t     -- Payment done Successfully -- ")
            except:
                  print("\t\t\t Oops , Something went Wrong!")                  
      def __del__(self):
            self.con.close()
            print("\t\t\t\tGood Day")
            print("\t\t\t *******  Thank You  ******* ")
