from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0

root= Tk()
root.geometry("555x325")
root.title("listbox ")

lbx= Listbox(root)
lbx.pack()
lbx.insert(END,"First item")



Button(root,text="ADD ITEM",command=add).pack()

root.mainloop()