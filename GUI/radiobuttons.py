from tkinter import *
import tkinter.messagebox as tmsg
root= Tk()
root.geometry("455x255")
root.title("radiobuttons")

def ordered():
    tmsg.showinfo("order recieved:",f"we have recieved your order for {var.get()} ,thanks for ordering")
# var=IntVar()
var=StringVar()
var.set("radio")
#var.set(1)
Label(root,text="what u want to eat?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="dosa",padx=60,variable=var,value="dosa").pack(anchor="w")
radio=Radiobutton(root,text="paranths",padx=60,variable=var,value="paranths").pack(anchor="w")
radio=Radiobutton(root,text="idly",padx=60,variable=var,value="idly").pack(anchor="w")
radio=Radiobutton(root,text="panner kulcha",padx=60,variable=var,value="panner kulcha").pack(anchor="w")

Button(text="order now",command=ordered).pack()

root.mainloop()