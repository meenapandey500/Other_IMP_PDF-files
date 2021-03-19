from tkinter import *
memory=""
def press(num):
    global memory
    memory=memory+str(num)
    x.set(memory)
def pressequal():
    global memory
    total = eval(memory)
    #eval() inbuilt function which convert string type value to numeric value
     #eval() ==>automatic evalute means + then +  ,- means -
    x.set(total)         
def pressclear():
    global memory
    memory= ""
    x.set(memory)
    
window=Tk()
window.title("Calculator")
window.geometry("300x300")
x=StringVar()
e1=Entry(window,textvariable=x)
#e1.pack()
#e1.place(x=50,y=50)
e1.grid(row=0,column=0,columnspan=4)

b1=Button(window,text="7",font=("arial black",7),command=lambda:press(7))
b1.grid(row=1,column=0)
b2=Button(window,text="8",font=("arial black",7),command=lambda:press(8))
b2.grid(row=1,column=1)
b3=Button(window,text="9",font=("arial black",7),command=lambda:press(9))
b3.grid(row=1,column=2)
b4=Button(window,text="+",font=("arial black",7),command=lambda:press("+"))
b4.grid(row=1,column=3)

b5=Button(window,text="4",font=("arial black",7),command=lambda:press(4))
b5.grid(row=2,column=0)
b6=Button(window,text="5",font=("arial black",7),command=lambda:press(5))
b6.grid(row=2,column=1)
b7=Button(window,text="6",font=("arial black",7),command=lambda:press(6))
b7.grid(row=2,column=2)
b8=Button(window,text="-",font=("arial black",7),command=lambda:press("-"))
b8.grid(row=2,column=3)

b9=Button(window,text="1",font=("arial black",7),command=lambda:press(1))
b9.grid(row=3,column=0)
b10=Button(window,text="2",font=("arial black",7),command=lambda:press(2))
b10.grid(row=3,column=1)
b11=Button(window,text="3",font=("arial black",7),command=lambda:press(3))
b11.grid(row=3,column=2)
b12=Button(window,text="=",font=("arial black",7),command=pressequal)
b12.grid(row=3,column=3)
b12=Button(window,text=".",font=("arial black",7),command=lambda:press("."))
b12.grid(row=4,column=1)
b13=Button(window,text="CLS",font=("arial black",7),command=pressclear)
b13.grid(row=4,column=2)
window.mainloop()
