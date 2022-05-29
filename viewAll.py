from tkinter import *
from tkinter import ttk
import connection
import delete
import updateui

def viewpat():
     
    def btnDel():
        window.destroy()
        delete.delpatUI() 

    def btnUpdate():
        window.destroy()
        updateui.updatePatDio()


    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View patient")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="patID:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="patName:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="phoneno:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="address:",padding=20,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="sex:",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Label(frm, text="date_admitted:",padding=10,relief="raised").grid(column=10, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
    ttk.Label(frm, text="date_discharged:",padding=10,relief="raised").grid(column=12, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=13, row=0)
    ttk.Label(frm, text="doc_id:",padding=10,relief="raised").grid(column=14, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=15, row=0)
    ttk.Label(frm, text="room_id:",padding=10,relief="raised").grid(column=16, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=17, row=0)


    lst = connection.patLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
        ttk.Label(frm, text=lst[i][5],padding=10,relief="flat").grid(column=10, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
        ttk.Label(frm, text=lst[i][6],padding=10,relief="flat").grid(column=12, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=13, row=0)
        ttk.Label(frm, text=lst[i][7],padding=10,relief="flat").grid(column=14, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=15, row=0)
        ttk.Label(frm, text=lst[i][8],padding=10,relief="flat").grid(column=16, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=17, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=12, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=15, row=i+1)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=14, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=16,row=i+2)

    window.mainloop()

def viewdoc():
    def btnDel():
        window.destroy()
        delete.deldocUI()
        
   
    def btnUpdate():
        window.destroy()
        updateui.updateDocDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View doctor")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields

    ttk.Label(frm, text="doc id:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="doc_name:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="address:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="blood_group",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="dob",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Label(frm, text="hosp id",padding=10,relief="raised").grid(column=10, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=11, row=0)


    lst = connection.docLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)        
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
        ttk.Label(frm, text=lst[i][5],padding=10,relief="flat").grid(column=10, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=11, row=0)


    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=6, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=8, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=10,row=i+2)

    window.mainloop()

def viewrooms():

    def btnDel():
        window.destroy()
        delete.delroomUI() 

    def btnUpdate():
        window.destroy()
        updateui.updateRoomDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View rooms")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="room ID:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="period:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="room type:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="price:",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="no of alloted pat:",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Label(frm, text="hosp id:",padding=10,relief="raised").grid(column=10, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=11, row=0)

    lst = connection.roomLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
        ttk.Label(frm, text=lst[i][5],padding=10,relief="flat").grid(column=10, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=6, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=8, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=10,row=i+2)

    window.mainloop()

def viewhos():
    def btnDel():
        window.destroy()
        delete.delhosUI() 
    def btnUpdate():
        window.destroy()
        updateui.updateHosDio()  

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View hospital")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="hos ID:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="name:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="City:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="specialization:",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="branch",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)

    lst = connection.hosLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=4, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=6, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=8,row=i+2)

    window.mainloop()

def viewmr():

    def btnDel():
        window.destroy()
        delete.delmrUI()
    
    
    def btnUpdate():
        window.destroy()
        updateui.updateMedDio()
    
    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View medical record")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="record no:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="blood_group:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="description:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="patient_no:",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="appointment:",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Label(frm, text="pid:",padding=10,relief="raised").grid(column=10, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
    
    lst = connection.mrLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
        ttk.Label(frm, text=lst[i][5],padding=10,relief="flat").grid(column=10, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=6, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=8, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=10,row=i+2)

    window.mainloop()