from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("500x250+500+200")
        self.root.resizable(False,False)
        Label(root, text="Login form", font="arial 15 bold",fg="red").grid(row=0, column=3)
        # background image
        # self.bg=ImageTk.PhotoImage(file="images/1.jpg")
        # self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # login frame
        # Frame_login= Frame(self.root,bg="white")
        # Frame_login.place(x=330,y=150,width=550,height=450)

        #title and subtitle
        # title=Label(Frame_login,text="login here",font=("Impact",35,"bold"),fg="red",bg="white").place(x=98,y=30)
        #for username
        Label(root, text="username",font ="arial 15 bold", fg="grey").grid(row=3, column=0)
        self.username=Entry(text="user name",font=("goudy old style ",15,"bold"),fg="grey",bg="white")
        self.username.place(x=100,y=32)
        #for pass
        Label(root, text="password", font="arial 15 bold", fg="grey").grid(row=6, column=0)
        self.password = Entry(text="password", font=("goudy old style ", 15, "bold"), fg="grey", bg="white")
        self.password.place(x=100, y=62)
        #button
        forget=Button(root, text="forget password?",font ="arial 12 ",bg="grey" ,fg="black").grid(row=8, column=1)
        Submit = Button(root,command=self.check_function, text="Submit", font="arial 12 ",bg="purple", fg="black").grid(row=8, column=3)
        print("accepted")
    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("error","All fields are required",parent=self.root)
        elif self.username.get() != "MCAstudent" and self.password.get()!= "mca2021":
            messagebox.showerror("error","enter both again", parent=self.root)
        elif self.username.get() != "MCAstudent" or self.password.get() != "mca2021":
            messagebox.showerror("error", "invalid username or password is ", parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome{self.username.get()}")


root=Tk()
obj=login(root)
root.mainloop()