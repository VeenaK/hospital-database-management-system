from cgitb import text
from email.mime import image
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import width

import hospital


checkUsername = 'veena'
checkPassword = '8431258285'

def loginWin():
    # onClick action
    def btn_click():
        username = username_enter.get()
        password = password_enter.get()
        # mainPage.win()
        if(username == checkUsername and password == checkPassword):
            window.destroy()
            hospital.win()
        else:
            messagebox.showerror(title="Error" , message="Invalid Credentials")

    # window creation
    window = Tk()

    # width = window.winfo_screenwidth()
    # height = window.winfo_screenheight()
    # # window.geometry("%dx%d" % (width,height))
    # # window.eval('tk::PlaceWindow . center')

    window.title("Login Page")

    

    window.geometry("1350x720")

    my_canvas = Canvas(window,width=1350,height=720)
    my_canvas.pack(fill="both",expand=True)
    bg1 = PhotoImage(file='frontpa.png')
    bg = bg1.subsample(1,1)

    my_canvas.create_image(0,0,image=bg,anchor="nw")
    my_canvas.create_text(500,90,text="",font=("bold",30),fill="red")

    # Labels
    my_canvas.create_text(625,100,text="USERNAME:",font=("bold",10),fill="black")
    my_canvas.create_text(625,150,text="PASSWORD:",font=("bold",10),fill="black")

    username_enter = Entry(window)
    my_canvas.create_window(740,100, window=username_enter)

    password_enter = Entry(window)
    my_canvas.create_window(740,150, window=password_enter)

    # Buttons
    #loginImg = PhotoImage(file=r"images/login.png").subsample(30,30)
    btn1 = Button(window, text="Login", command=btn_click)

    #logoutImg = PhotoImage(file=r"images/logout.png").subsample(30,30)   
    btn2 = Button(window, text="Exit", command=window.destroy)

    btn1_win = my_canvas.create_window(675,190, window=btn1)
    btn2_win = my_canvas.create_window(675,230, window=btn2)

    
    window.mainloop()
    

loginWin()