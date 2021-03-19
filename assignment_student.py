#Create a class Student that will accept Student Name and Course Joined.
#Note the data members have to be strongly private.

Create constructor and destructor

Functions to input and display information of the student
class Student: #Employee user defined class name
    def getdata(self):
        self.__name=input("Enter Student name : ")
        self.__Course=input("Enter Course name : ")

    def display(self):
        print("Student Name : ",self.__name)
        print("Course Name : ",self.__Course)

#main program
stud1=Student()  #here stud1 object name of Student class
print("Enter First student Details : ")
stud1.getdata()

print("student First Details : ")
stud1.display()

stud2=Student() #here stud2 object name of Student class

print("Enter Second Student Details : ")
stud2.getdata()
print("Print Second Student Details : ")
stud2.display()
