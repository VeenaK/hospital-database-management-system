from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import hospital

checkUsername = 'veena'
checkPassword = '8431258285'

# onClick action
def btn_click():
    username = username_enter.get()
    password = password_enter.get()
    if(username == checkUsername and password == checkPassword):
       hospital.win()
       window.destroy()
    else:
         messagebox.showerror(title="Error" , message="Invalid Credentials")



# window creation
window = Tk()


window.title("Login Page")

# frame creation
frm = ttk.Frame(window,padding=20)
frm.grid()

# Labels, Buttons and textEntry
ttk.Label(frm,text="User Name:",padding=10).grid(column=0,row=0)
username_enter = Entry(frm)
username_enter.grid(column=1,row=0)

ttk.Label(frm,text="Password:",padding=10).grid(column=0,row=1)
password_enter = Entry(frm)
password_enter.grid(column=1,row=1)

loginBtn = ttk.Button(frm, text="Login", command=btn_click)
loginBtn.grid(column=1,row=3)

exitBtn = ttk.Button(frm, text="Exit", command=window.destroy)
exitBtn.grid(column=1,row=4)

window.mainloop()