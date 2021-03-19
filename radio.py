
from tkinter.messagebox import *
def save():
    
    fname=fnametxt.get()
    lname=lnametxt.get()
    g=gender.get()
    
    
from tkinter import *

#object of window 
win=Tk()
win.title("Demo Window")
win.geometry("700x700")

fname = Label(win,text="First Name",bg="yellow",fg="blue",font=("Arial Black",20))
fname.grid(column=0,row=0)
lname = Label(win,text="Last Name",bg="yellow",fg="blue",font=("Arial Black",20))
lname.grid(column=0,row=1)
fnametxt=Entry(win,width=20,font=("Arial Black",20))
fnametxt.grid(column=1,row=0)
lnametxt=Entry(win,width=20,font=("Arial Black",20))
lnametxt.grid(column=1,row=1)
gender=StringVar()
male=Radiobutton(win,text="Male",value="male",variable=gender,font=("Arial Black",15),bg="yellow",fg="blue")
male.grid(column=0,row=2)
female=Radiobutton(win,text="FeMale",value="female",variable=gender,font=("Arial Black",15),bg="yellow",fg="blue")
female.grid(column=1,row=2)
save=Button(win,text="SAVE",font=("Arial Black",15),bg="yellow",fg="blue",command=save)
save.grid(column=0,row=3)
#infinite loop open window till user close it
win.mainloop()


    
