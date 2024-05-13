from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image, ImageFilter

from tkinter import messagebox
import os
import shutil
import sys

global entry1
global load_screen
bg_c='#3d6466'

##Functions
#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#window adjuster
def adjuster(event):
    # Get screen width and height
    
    screen_w = root.winfo_screenwidth()
    screen_h= root.winfo_screenheight()


    new_w= int(screen_w* 0.25)
    new_h= int(screen_h * 0.35)
    x = (screen_w - new_w) // 2
    y = (screen_h - new_h) // 2

    # new size and position
    root.geometry(f"{new_w}x{new_h}+{x}+{y}")
    
#main window
def mainwin():
    
    root.destroy()
    mainroot = tk.Tk()
    def adjuster(event):
    # Get screen width and height
    
        screen_w = mainroot.winfo_screenwidth()
        screen_h= mainroot.winfo_screenheight()


        new_w= int(screen_w* 0.25)
        new_h= int(screen_h * 0.35)
        x = (screen_w - new_w) // 2
        y = (screen_h - new_h) // 2

        mainroot.geometry(f"{new_w}x{new_h}+{x}+{y}")
    mainroot.title('The Organizer')
    mainroot.eval('tk::PlaceWindow . center')
    frame1 = Frame(mainroot,width=500,height=600,bg=bg_c)
    frame1.grid(row=0,column=0)
    frame1.pack_propagate(False)
    #picture
    pic=ImageTk.PhotoImage(file=resource_path("ROBOT.png"))
    pic_widget= tk.Label(frame1,image=pic,bg=bg_c)

    pic_widget.image=pic
    pic_widget.pack()
    tk.Label(
        frame1,
        text='Wanna organize your files?',
        bg=bg_c,
        fg='skyblue',
        font=('Wizard',14),
    ).pack()
    tk.Label(frame1,
    text='tell the path of folder u wanna organise',
    bg=bg_c,
    fg='skyblue',
    font=('wizard',14)
    ).pack()


    entry1= Entry(
        frame1,
        bg=bg_c,
        fg='skyblue',
        width=40,
        font=('Wizard',15)
    )
    entry1.pack()
    load_screen = Label(frame1,
                        text="...",
                        bg=bg_c,
                        fg='skyblue',
                        font=('Wizard',
                            12))
    load_screen.pack()
    summit=Button(
        frame1,
        command=lambda: onclick(load_screen,entry1),
        text='Organize this directory',
        bg=bg_c,
        fg='skyblue',
        width=20,
        font=('Wizard',15)
    )
    summit.pack()
    mainroot.bind("<Configure>", adjuster)
    mainroot.mainloop()



def onclick(load_screen,entry1):
    
    try:
        
        load_screen.config(text="...")
        path = entry1.get()
        files = os.listdir(path)
        if not os.path.exists(path):
            messagebox.showerror('stop fooling write the correct path')
            return
        load_screen.config(text="will be done oranizing files shortly.")
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]  # remove the dot from the extension
            if os.path.exists(os.path.join(path, extension)):  # Check if extension directory exists
                shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
                
            else:
                os.makedirs(os.path.join(path, extension))  # Create extension directory
                shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
        load_screen.config(text="your files are organized.")
        messagebox.showinfo("congratulation on your clean computer")
        entry1.delete(0,'end')
    except Exception as e:
        # Hide loading message on error
        load_screen.config(text="")
        messagebox.showerror("Error", str(e))

    


#first window
root = tk.Tk()

root.title('The Organizer')

root.eval('tk::PlaceWindow . center')
frame1 = Frame(root,width=500,height=600,bg=bg_c)
frame1.grid(row=0,column=0)
frame1.pack_propagate(False)
#picture
pic1=ImageTk.PhotoImage(file=resource_path("image2.png"))

pic1_widget= tk.Label(frame1,image=pic1,bg=bg_c)

pic1_widget.image=pic1
pic1_widget.pack()
tk.Label(frame1,
text='''HELLO AND WELLCOME TO THIS FILE ORGANIZING APP 
        Pls click the button bellow to continue''',
bg=bg_c,
fg='skyblue',
font=('wizard',11,'bold')
).pack()

continue_button=Button(
        frame1,
        command=mainwin,
        text='click me if u want continue',
        bg=bg_c,
        fg='skyblue',
        width=20,
        font=('Wizard',15)
    )
continue_button.pack()




root.bind("<Configure>", adjuster)

root.mainloop()