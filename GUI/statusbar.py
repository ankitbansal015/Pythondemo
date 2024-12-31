from tkinter import *
def upload():
    statusvar.set("busy..")
    import time
    time.sleep(2)
    statusvar.set("ready now")
root= Tk()
root.geometry("555x325")
root.title("statusbar")



statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()

root.mainloop()