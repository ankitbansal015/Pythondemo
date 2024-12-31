from tkinter import *
root=Tk()
def getvals():
    print("it works")
root.geometry("366x266")

Label(root,text="Welcome to pycharm",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
name=Label(root,text="Name").grid(row=1,column=2)
gender=Label(root,text="gender").grid(row=2,column=2)
emergency=Label(root,text="emergency contact").grid(row=3,column=2)
paymentmode=Label(root,text="payment mode").grid(row=4,column=2)

namevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry= Entry(root, textvariable=namevalue).grid(row=1,column=3)
genderentry= Entry(root, textvariable=gendervalue).grid(row=2,column=3)
emergencyentry= Entry(root, textvariable=emergencyvalue).grid(row=3,column=3)
paymentmodeentry= Entry(root, textvariable=paymentmodevalue).grid(row=4,column=3)
#checkbox
foodservice=Checkbutton(text="Want to prebook your meals?",variable=foodservicevalue,).grid(row=6,column=3)
#button and packing it and assinging it a command

Button(text="Submit ",command=getvals).grid(row=7,column=3)

root.mainloop()
