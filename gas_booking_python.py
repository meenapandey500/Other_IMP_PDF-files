'''First created payroll database and employee table, in table created column name in
sequence like (id,name,designation,basic_salary,da,hra,gross_salary,tax,net_salary  '''

print("    ------Project Title------     ")
print("------Gas Booking System System------")
input() #to hold the output screen
print(" *****Created by Chnmay Lakhote***** ")
print("-Using Python Programming Language-")
input() #to hold the output screen

import pymysql #To create a connection string (between python and mysqlserver)
import datetime #used for current date and time
#from tabulate import tabulate #used for get the data in the form of table
import warnings
warnings.filterwarnings('ignore')
servername="localhost"
username="root"
password=""
dbname="gasbooking"
try:
    con=pymysql.connect(servername,username,password,dbname)
except:
    print("Mysql server Connectivity Error")
else:
    print("Mysql server Connect Successfully.")
#main program
while(True):
    print("\n*****Gas Booking System: Main Menu*****")
    print("\t\t\t\t1. Add Booking Details")
    print("\t\t\t\t2. Exit")
    print("Enter Choice: ",end="") 
    choice=int(input())
    if choice==1:
        try: #use try
            print("Enter your details: ")
            cust_name=input("Enter Customer Name: ")
            cust_id=int(input("Enter 5 digit Customer Id: "))
            if(len(str(cust_id))==5):
               ph_number=int(input("Enter your 10 digit mobile number: "))
               ph_number=str(ph_number)
               x=len(ph_number)
               if(x==10):
                 #book_date=datetime.datetime.now()
                 book_date=datetime.datetime.today()
                 expected_delivery=book_date+datetime.timedelta(7)
                 book_date=str(book_date)
                 expected_delivery=expected_delivery.strftime('%Y-%m-%d')
                
                 
               else:
                   print("Incorrect mobile number")
            else:
                print("Entered incorrect customer id")
            pay_details=int(input("Press # 1 for COD ;#2 for Online payment"))
            if(pay_details==1):
                print("Gas booked sucussfully")
            elif(pay_details==2):
                print("enter 5 digit transaction number")
                tran_nu=int(input("Enter 5 digit transaction number:"))
                y=len(str(tran_nu))
                if(y==5):
                    print("gas booked succesfully")
                else:
                    print("Wrong transaction id")
            else:
                print("Wrong payment input")
                
            
            query="INSERT INTO bookingdetails(cust_name,cust_id,ph_number,book_date,expected_delivery,pay_details)values(%s,%s,%s,%s,%s,%s)"
            val=(cust_name,cust_id,ph_number,book_date,expected_delivery,pay_details)
            #val tuple variable
            #Prepare cursor
            cur=con.cursor()
            #Run insert query
            try:
                cur.execute(query,val)
            except:
                print("Query Error")
            else:
                con.commit() #Save in database used commit()
                print("gas booked Successfully")
        except:
            print('something went wrong')
    elif(choice==2):
        break
            
