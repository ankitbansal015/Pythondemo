from tkinter import *
root = Tk()
root.geometry("555x456")
f1=Frame(root,bg="red",borderwidth=9,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root,borderwidth=7,bg="grey",relief=SUNKEN)

f2.pack(side=TOP,fill="x")

l1=Label(f1,text="PROJECT tkinter - PYCHARM")
l1.pack(pady=150)
l2=Label(f2,text="WELCOME TO SUBLIME TEXT",font="Helvetica 16 bold",fg="red")
l2.pack()
root.mainloop()
