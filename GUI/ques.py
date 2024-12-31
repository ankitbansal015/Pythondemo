from tkinter import *
def update():
    print("updating gui")
    root.geometry(f"{width.get()}x{height.get()}")

root= Tk()
root.geometry("456x325")
root.title("exercise")
width=StringVar()
height=StringVar()

Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="Apply",command=update).pack()

root.mainloop()