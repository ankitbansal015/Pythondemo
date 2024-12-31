from tkinter import *
root=Tk()
root.geometry("700x566")
root.title("menus")
def myfunc():
    print("hello pycharm")
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


root.mainloop()