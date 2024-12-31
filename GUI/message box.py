from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("700x566")
root.title("menus")
def myfunc():
    print("hello pycharm")

def help():
    print("i will help you")
    tmsg.showinfo("help","ankit will help u")

def rate():
    print("rate us")
    value=tmsg.askquestion(" was your experience good","u use this gui... was your experience good")
    if value=="yes":
        msg="great.rate us at palystore"
    else:
        msg ="tell us what is wrong we will resolve it"
    tmsg.showinfo("experience",msg)
    print(value)
    #use these for non dropdown menu
# mymenu=Menu(root)
# mymenu.add_command(label="file",command=myfunc)
# mymenu.add_command(label="exit",command=quit)
# root.config(menu=mymenu)
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="new project",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_separator()
m1.add_command(label="save as",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="file",menu=m1)


m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="paste",command=myfunc)
m2.add_command(label="copy",command=myfunc)
m2.add_separator()
m2.add_command(label="cut",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="rate us",command=rate)
mainmenu.add_cascade(label="help",menu=m3)
root.config(menu=mainmenu)
root.mainloop()