from tkinter import *
from tkinter import ttk
import viewAll
import addnew


def win():
   # window creation
    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("hospital")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # hospital
    hosRow = 0
    ttk.Label(frm,text="hospital",padding=10).grid(column=0,row=hosRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=hosRow)

    addhosBtn = ttk.Button(frm, text="Add New", command=addnew.addhos)
    addhosBtn.grid(column=2,row=hosRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=hosRow)
    
    viewAllhosBtn = ttk.Button(frm, text="View All", command=viewAll.viewhos)
    viewAllhosBtn.grid(column=4,row=hosRow)

    # Medical Record
    secRow = 5
    ttk.Label(frm,text="Medical Record",padding=10).grid(column=0,row=secRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=secRow)

    addSecBtn = ttk.Button(frm, text="Add New", command=addnew.addmr)
    addSecBtn.grid(column=2,row=secRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=secRow)
    
    viewAllSecBtn = ttk.Button(frm, text="View All", command=viewAll.viewmr)
    viewAllSecBtn.grid(column=4,row=secRow)

    # doctor
    docRow = 2
    ttk.Label(frm,text="doctor",padding=10).grid(column=0,row=docRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=docRow)

    addhosBtn = ttk.Button(frm, text="Add New", command=addnew.adddoc)
    addhosBtn.grid(column=2,row=docRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=docRow)
    
    viewAllhosBtn = ttk.Button(frm, text="View All", command=viewAll.viewdoc)
    viewAllhosBtn.grid(column=4,row=docRow)

    # rooms
    roomRow = 3
    ttk.Label(frm,text="rooms",padding=10).grid(column=0,row=roomRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=roomRow)

    addhosBtn = ttk.Button(frm, text="Add New", command=addnew.addroom)
    addhosBtn.grid(column=2,row=roomRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=roomRow)
    
    viewAllroomBtn = ttk.Button(frm, text="View All", command=viewAll.viewrooms)
    viewAllroomBtn.grid(column=4,row=roomRow)

    # patient
    patRow = 4
    ttk.Label(frm,text="patient",padding=10).grid(column=0,row=patRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=patRow)

    addpatBtn = ttk.Button(frm, text="Add New", command=addnew.addpat)
    addpatBtn.grid(column=2,row=patRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=patRow)
    
    viewAllpatBtn = ttk.Button(frm, text="View All", command=viewAll.viewpat)
    viewAllpatBtn.grid(column=4,row=patRow)


    window.mainloop()
