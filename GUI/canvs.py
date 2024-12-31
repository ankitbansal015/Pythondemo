from tkinter import *

root=Tk()
canvas_width=800
canvas_hight=400

root.geometry(f"{canvas_width}x{canvas_hight}")
root.title("ankit ka gui")
can_widget=Canvas(root,width=canvas_width,height=canvas_hight)
can_widget.pack()
# the line goes from the point x1,y1,to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="blue")
# if u want to create rectangle specify parameters in  this orders- coord pf topleft and of bottomright
can_widget.create_rectangle(3,5,700,300,fill="red")

can_widget.create_text(200,200,fill="blue",text="python")

can_widget.create_oval(5,5,200,200)


root.mainloop()