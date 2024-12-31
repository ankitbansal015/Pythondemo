from tkinter import *
root = Tk()
root.geometry("500x500")

def getvals():
    print("Accepted")
#heading
Label(root, text="Registration form", font="arial 15 bold").grid(row=0,column=3)

#field name
name = Label(root,text="Name")
fathername = Label(root,text="Father Name")
phonenum = Label(root,text="Phone num")
gender = Label(root,text="Gender")
paymentmode = Label(root,text="Payment mode")
#packing fields
name.grid(row=1,column=2)
fathername.grid(row=2,column=2)
phonenum.grid(row=3,column=2)
gender.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)
#variable for storing data
namevalue= StringVar
fathernamevalue= StringVar
phonenumvaluevalue= StringVar
gendervalue= StringVar
paymentmodevalue= StringVar
checkvalue=IntVar
#creating entry field

nameentry= Entry(root, textvariable=namevalue)
fathernameentry= Entry(root, textvariable=fathernamevalue)
phonenumentry= Entry(root, textvariable=phonenumvaluevalue)
genderentry= Entry(root, textvariable=gendervalue)
paymentmodeentry= Entry(root, textvariable=paymentmodevalue)
#packing entry fields
nameentry.grid(row=1,column=3)
fathernameentry.grid(row=2,column=3)
phonenumentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)
#creating checkbox
checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#submit button
Button(text="Submit",command=getvals).grid(row=7,column=3)

root.mainloop()