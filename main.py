from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog

root=Tk()
root.title("WHITE BOARD")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False,False)

current_x=0
current_y=0
color="black"

def locate_xy(work):
    global  current_x,current_y

    current_x = work.x
    current_y =work.y

def addline(work):
    global current_x,current_y

    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=True)
    current_x,current_y=work.x,work.y
def show_color(new_color):
    global color

    color=new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()

#icon
image_icon = PhotoImage(file="img/logo.png")
root.iconphoto(False,image_icon)

##sidebar
color_box = PhotoImage(file="img/section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=30)

eraser=PhotoImage(file="img/eraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=20,y=465)

addImg=PhotoImage(file="img/addimage.png")
Button(root,image=addImg,bg="#f2f3f5").place(x=20,y=400)

###########colors
colors=Canvas(root,bg="#fff",width=50,height=350,bd=0)
colors.place(x=22,y=40)

def display_pallete():
    id=colors.create_rectangle((15,15,35,35),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id = colors.create_rectangle((15, 45, 35, 65), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((15, 75, 35, 95), fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((15, 105, 35, 125), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((15, 135, 35, 155), fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((15, 165, 35, 185), fill="pink")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('pink'))

    id = colors.create_rectangle((15, 195, 35, 215), fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

    id = colors.create_rectangle((15, 225, 35, 245), fill="gold")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gold'))

    id = colors.create_rectangle((15, 255, 35, 275), fill="gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((15, 285, 35, 305), fill="brown")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown'))

    id = colors.create_rectangle((15, 315, 35, 335), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

display_pallete()

##main screen
canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=30)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addline)

###########slider############
current_value=tk.DoubleVar()
def get_current_value():
    return'{: .2f}'.format(current_value.get())
def slider_changed(event):
    value_label.configure(text=get_current_value())

slider=ttk.Scale(root,from_=0,to=100,orient="horizontal",command=slider_changed,variable=current_value)
slider.place(x=10,y=530)

value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=10,y=550)

root.mainloop()