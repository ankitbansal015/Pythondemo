from tkinter import *
from PIL import ImageTk,Image
def every_50(text):
    final_text=""
    for i in range(0,len(text)):
        final_text +=text[i]
        if i%50==0 and i!=0:
            final_text +="\n"
    return final_text
root=Tk()
root.title("appka apna akhbaar")
root.geometry("900x700")
texts=[]
photos=[]
for i in range (0,3):
    with open (f"news.txt")as f:
        text=f.read()
        texts.append(every_50(text))
    image=Image.open(f"download.png")
#TODO:resize images
    image=image.resize((350,265),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
f0=Frame(root,width=600,height=70)
Label(f0,text="profile of virat kohli",font="lucida 25 bold").pack()
f0.pack()

f1=Frame(root,width=700,height=150)
Label(f1,text=texts[0],padx=100,pady=0).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack(side="right")
f1.pack(anchor="w")

root.mainloop()