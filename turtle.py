import pymysql

con=pymysql.connect('localhost','root','','mydata')
cursor=con.cursor()

a=('update users set mobile=%s where id=2')
b=int(input('enter number'))
cursor.execute(a,b)
cursor.execute('select * from users')
result=cursor.fetchall()
for i in result:
    print(i)
##print(result)
id1=int(input('enter id'))
name=input('enter your name')
dob=input('enter dob')
mobile=input('enter mobile')
email=input('enter email')

cursor.execute('insert into users values({},"{}","{}","{}","{}")'.format(id1,name,dob,mobile,email))
con.commit()
print('insert successfull')
con.close()
