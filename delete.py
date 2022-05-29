import cx_Oracle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection
import viewAll

def delData(tabName,idName,id):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('delete from {} where {} = {}'.format(tabName,idName,id))
    conn.commit()
    conn.close()

def delpatUI():

    def btnDelCick():
        id = id_enter.get()
        delData('patient','pid' ,id)
        messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
        window.destroy()
        viewAll.viewpat()
    
    def btnCanClick():
        window.destroy()
        viewAll.viewpat()

    window = Tk()
    window.title("Delete patient")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter patient ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def deldocUI():

    def btnDelCick():
        id = id_enter.get()
        delData('doctor', 'doc_id' , id)
        messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
        window.destroy()
        viewAll.viewdoc()
    
    def btnCanClick():
        window.destroy()
        viewAll.viewdoc()

    window = Tk()
    window.title("Delete doctor")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter doctor No to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delroomUI():

    def btnDelCick():
        id = id_enter.get()
        delData('rooms', 'room_id' , id)
        messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
        window.destroy()
        viewAll.viewroom()
    
    def btnCanClick():
        window.destroy()
        viewAll.viewroom()

    window = Tk()
    window.title("Delete room")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter room ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delhosUI():
    
    def btnDelCick():
        id = id_enter.get()
        delData('hospital', 'hosp_id' , id)
        messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
        window.destroy()
        viewAll.viewhos()
    
    def btnCanClick():
        window.destroy()
        viewAll.viewhos()

    window = Tk()
    window.title("Delete  hospital")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter hospital ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delmrUI():

    def btnDelCick():
        id = id_enter.get()
        delData('medical_record', 'record_no' , id)
        messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
        window.destroy()
        viewAll.viewmr()
    
    def btnCanClick():
        window.destroy()
        viewAll.viewmr()

    window = Tk()
    window.title("Delete medical record")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter record no to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()
