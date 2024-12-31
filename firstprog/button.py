from tkinter import *
root =Tk()
root.geometry("555x456")
def hello():
    print("hello tkinter button")
def name():
    print("NAme is ankit")
f1=Frame(root,bg="red",borderwidth=9,relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")
b1=Button(f1,fg="red",text="print now",command=hello)
b1.pack(side=LEFT,padx=20)
b3=Button(f1,fg="red",text="tell me your name",command=name)
b3.pack(side=LEFT,padx=20)
b2=Button(f1,fg="red",text="print now",command=hello)
b2.pack(side=LEFT,padx=20)


root.mainloop()