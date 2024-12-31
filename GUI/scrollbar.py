from tkinter import *
root= Tk()
root.geometry("555x325")
root.title("scrollbar")
# fro connecting scrollbar to a widget
#1. widget(yscrollcommand=scrollbar.set)
#2. scrollbar.config(command=widget,yview)

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"item {i}")

listbox.pack(fill="both",padx=22)
scrollbar.config(command=listbox.yview)
root.mainloop()