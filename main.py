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

#icon
image_icon = PhotoImage(file="img/logo.png")
root.iconphoto(False,image_icon)

##sidebar
color_box = PhotoImage(file="img/section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=30)



##main screen
canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=30)



root.mainloop()