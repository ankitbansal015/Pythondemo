from tkinter import  *
root=Tk()
root.geometry("444x233")
root.title("my gui")
#title
# title_label=Label(text="hello to gui",bg="red",fg="white",padx=23,pady=20,font=("comicsansms",15,"bold"))
title_label=Label(text="hello to gui",bg="red",fg="white",padx=23,pady=20,font="comicsansms 15 bold",borderwidth=10,relief=SUNKEN)
#imporatnt pack options , anchor=sw, side= top bottom left right
#fill,padx,pady

title_label.pack(side=BOTTOM,anchor="nw",fill=X,padx=45,pady=56)

root.mainloop()