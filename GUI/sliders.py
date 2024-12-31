from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("slider")

def getdollars():
    print(f"we have credited {myslider.get()} dollars to your bank account")
    tmsg.showinfo("amount credited",f"we have credited {myslider.get()} dollars to your bank account")

Label(root,text="how many dollars do u want").pack()

myslider=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=20)
# myslider.set(22)
myslider.pack()
# myslider2=Scale(root,from_=0,to=100)
# myslider2.pack()

Button(root,text="get dollars",command=getdollars).pack()

root.mainloop()