from tkinter import *
def getvals():
    print("the value of username is",{uservalue.get()})
    print("the value of password is",{passvalue.get()})
root=Tk()
root.geometry("555x456")
username=Label(root,text="username").grid(row=0,column=0)
passsword=Label(root,text="password").grid(row=1)
#variable clases in tkinter  1= boolean var 2= double var 3= itnvar 4= strvar
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue).grid(row=0,column=1)
passentry=Entry(root,textvariable=passvalue).grid(row=1,column=1)
Button(text="Submit",command=getvals).grid()
root.mainloop()