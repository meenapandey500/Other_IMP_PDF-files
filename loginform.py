from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)#Set __init__ to the master class
        self.grid()
        self.create_main()#Creates function

    def create_main(self):
        print("testing")
        self.title = Label(self, text=" Stuck In The Circle ")#TITLE 
        self.title.grid(row=0, column=2)

        self.user_entry_label = Label(self, text="Username: ")#USERNAME LABEL
        self.user_entry_label.grid(row=1, column=1)

        self.user_entry = Entry(self)                        #USERNAME ENTRY BOX
        self.user_entry.grid(row=1, column=2)

        self.pass_entry_label = Label(self, text="Password: ")#PASSWORD LABEL
        self.pass_entry_label.grid(row=2, column=1)

        self.pass_entry = Entry(self)                        #PASSWORD ENTRY BOX
        self.pass_entry.grid(row=2, column=2)

        self.sign_in_butt = Button(self, text="Sign In",command = self.logging_in)#SIGN IN BUTTON
        self.sign_in_butt.grid(row=5, column=2)

    def logging_in(self):
        
        u = self.user_entry.get()#Retrieve Username
        p = self.pass_entry.get()#Retrieve Password
        if(u=="" and p==""):
            messagebox.showerror("Error","All Fields are required",parent=root)
        elif(u=="" or p=="1234"):
            messagebox.showerror("Error","Invalid username and password",parent=root)
        elif(u == 'rekha' and p == '123'):
                messagebox.showinfo("Login","Welcome!")
#Main
root = Tk()
root.title("Stuck in the Circle")
root.geometry("400x100")

app = Application(root)#The frame is inside the widgit
root.mainloop()#Keeps the window open/running
