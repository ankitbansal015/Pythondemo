from tkinter import *
def harry(event):
    print(f"u cliked on the button at {event.x} ,{event.y}")
root=Tk()
root.title("events in tkinter")
root.geometry("644x344")
widget=Button(root,text='click me')
widget.pack()
widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)
root.mainloop()