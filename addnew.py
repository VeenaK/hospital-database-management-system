from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection
import adddata



# Add patient
def addpat():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(patpidEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='patient ID cannot be Empty')
        else:
            pid = patpidEtr.get()
        if(patNameEtr.get() == ''):
           name=''
        else:
           name = patNameEtr.get()
        if(pataddressEtr.get() == ''):
            address = ''
        else:
            address = pataddressEtr.get()
        if(patSexEtr.get() == ''):
            sex = ''
        else:
            sex = patSexEtr.get()
        if(patadmEtr.get() == ''):
            date_admitted = ''
        else:
           date_admitted = patadmEtr.get()
        if(phoneEtr.get() == ''):
            contact_no = ''
        else:
             contact_no = phoneEtr.get()

        if(patdisidEtr.get() == ''):
            discharged_date = ''
        else:
            discharged_date= patdisidEtr.get()
        if(patdocEtr.get() == ''):
            doc_id= ''
        else:
            doc_id = patdocEtr.get()

        if(patroomEtr.get() == ''):
            room_id= ''
        else:
            room_id = patroomEtr.get()
                
        # print(empId + " " + empName + " " +address + " " +sex + " " + salary + " " +phoneNo + " " +mgrId + " " + secNo)
        # print(type(salary))

        adddata.addpatient(pid,name,contact_no,address,sex,date_admitted ,discharged_date ,doc_id,room_id )

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New patient")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="patient pid:",padding=10).grid(column=0, row=0)
    patpidEtr = Entry(frm)
    patpidEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="patient Name:",padding=10).grid(column=0, row=1)
    patNameEtr = Entry(frm)
    patNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Phone No:",padding=10).grid(column=0, row=2)
    phoneEtr = Entry(frm)
    phoneEtr.grid(column = 1, row = 2)


    ttk.Label(frm, text="Address:",padding=10).grid(column=0, row=3)
    pataddressEtr = Entry(frm)
    pataddressEtr.grid(column = 1, row = 3)

    
    ttk.Label(frm, text="Sex:",padding=10).grid(column=0, row=4)
    sex = ['M' , 'F']
    patSexEtr = ttk.Combobox(frm,values=sex,width=15)
    patSexEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="date admitted:",padding=10).grid(column=0, row=5)
    patadmEtr = Entry(frm)
    patadmEtr.grid(column = 1, row = 5)

   
    ttk.Label(frm, text="date discharged:",padding=10).grid(column=0, row=6)
    patdisidEtr = Entry(frm)
    patdisidEtr.grid(column = 1, row = 6)

    ttk.Label(frm, text="doc_id:",padding=10).grid(column=0, row=7)
    patdocEtr = Entry(frm)
    patdocEtr.grid(column = 1, row = 7)

    ttk.Label(frm, text="room_id:",padding=10).grid(column=0, row=8)
    patroomEtr = Entry(frm)
    patroomEtr.grid(column = 1, row = 8)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=10)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=10)

    window.mainloop()

# Add doctor
def adddoc():

    def cancelBtn():
      window.destroy()

    def addBtn():
        if(docidEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='doc id cannot be Empty')
        else:
            doc_id = docidEtr.get()
        
        if(docnameEtr.get() == ''):
            name = ''
        else:
             name = docnameEtr.get()
        
        if(docaddrEtr.get() == ''):
            address = ''
        else:
            address = docaddrEtr.get()
        
        if(docbgroupEtr.get() == ''):
           blood_group = ''
        else:
           blood_group = docbgroupEtr.get()

        if(docdobEtr.get() == ''):
           dob = ''
        else:
            dob = docdobEtr.get()
        if(dochidEtr.get() == ''):
          hosp_id= ''
        else:
           hosp_id = dochidEtr.get()


        adddata.adddoctor(doc_id,name,address,blood_group,dob,hosp_id)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New S")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="doc_id:",padding=10).grid(column=0, row=0)
    docidEtr = Entry(frm)
    docidEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="address:",padding=10).grid(column=0, row=1)
    docaddrEtr = Entry(frm)
    docaddrEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="blood group:",padding=10).grid(column=0, row=2)
    docbgroupEtr = Entry(frm)
    docbgroupEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="dob:",padding=10).grid(column=0, row=3)
    docdobEtr = Entry(frm)
    docdobEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="name:",padding=10).grid(column=0, row=4)
    docnameEtr = Entry(frm)
    docnameEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="hosp_id:",padding=10).grid(column=0, row=5)
    dochidEtr = Entry(frm)
    dochidEtr.grid(column = 1, row = 5)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=6)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=6)

    window.mainloop()

# Add rooms
def addroom():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(roomIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='room ID cannot be Empty')
        else:
          room_Id = roomIdEtr.get()
        if(roomperiodEtr.get() == ''):
            room_period= ''
        else:
           room_period = roomperiodEtr.get()
        if(roomtypeEtr.get() == ''):
           room_type = ''
        else:
            room_type = roomtypeEtr.get()
        if(priceEtr.get() == ''):
            price = ''
        else:
            price = priceEtr.get()
        if(priceEtr.get() == ''):
            price = ''
        else:
            price = priceEtr.get()
        if(allotpatEtr.get() == ''):
            allot_pat = ''
        else:
            allot_pat= allotpatEtr.get()
        if(roomhosidEtr.get() == ''):
           hosp_id = ''
        else:
            hosp_id = roomhosidEtr.get()
        

        adddata.addrooms(room_Id, room_period, room_type, price, allot_pat,hosp_id)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()


    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New room")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="room ID:",padding=10).grid(column=0, row=0)
    roomIdEtr = Entry(frm)
    roomIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="period:",padding=10).grid(column=0, row=1)
    roomperiodEtr = Entry(frm)
    roomperiodEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="roomtype:",padding=10).grid(column=0, row=2)
    roomtypeEtr = Entry(frm)
    roomtypeEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="price:",padding=10).grid(column=0, row=3)
    priceEtr = Entry(frm)
    priceEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="no of alloted pat",padding=10).grid(column=0, row=4)
    allotpatEtr = Entry(frm)
    allotpatEtr.grid(column = 1, row = 4)

    
    ttk.Label(frm, text="hosid",padding=10).grid(column=0, row=5)
    roomhosidEtr = Entry(frm)
    roomhosidEtr.grid(column = 1, row = 5)



    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=6)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=6)

    window.mainloop()

# Add hospital
def addhos():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(hosIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Supplier ID cannot be Empty')
        else:
           hos_Id= hosIdEtr.get()
        if(nameEtr.get() == ''):
           name = ''
        else:
            name = nameEtr.get()
        if(cityEtr.get() == ''):
           city = ''
        else:
             city =  cityEtr.get()
        if(specEtr.get() == ''):
            spec = ''
        else:
            spec = specEtr.get()
        if(branchEtr.get() == ''):
           branch = ''
        else:
            branch = branchEtr.get()

        adddata.addhospital(hos_Id, name, city, spec, branch)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()


    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New hospital")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="hosp ID:",padding=10).grid(column=0, row=0)
    hosIdEtr = Entry(frm)
    hosIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="name:",padding=10).grid(column=0, row=1)
    nameEtr = Entry(frm)
    nameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="City:",padding=10).grid(column=0, row=2)
    cityEtr = Entry(frm)
    cityEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="specialization:",padding=10).grid(column=0, row=3)
    specEtr = Entry(frm)
    specEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="branch:",padding=10).grid(column=0, row=4)
    branchEtr = Entry(frm)
    branchEtr.grid(column = 1, row = 4)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)


    window.mainloop()

# Add medical record
def addmr():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(bgEtr.get() == ''):
           blood_group=''
        else:
           blood_group =bgEtr.get()
        if(descEtr.get() == ''):
           description = ''
        else:
           description  =  descEtr.get()
        if(rnoEtr.get() == ''):
           messagebox.showwarning(title='Primary Key', message='Employee ID cannot be Empty')
        else:
            record_no =int(rnoEtr.get())
        if(patdEtr.get() == ''):
            patient_no = ''
        else:
            patient_no=patdEtr.get()
        if(appEtr.get() == ''):
           appointment = ''
        else:
            appointment=appEtr.get()
        if(mrpidEtr.get() == ''):
            pid = ''
        else:
            pid = mrpidEtr.get()

        
        adddata.addmedical_record(blood_group, description, record_no, patient_no, appointment, pid)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()


    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New medical record")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields

    ttk.Label(frm, text="blood group:",padding=10).grid(column=0, row=0)
    bgEtr = Entry(frm)
    bgEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="description:",padding=10).grid(column=0, row=1)
    descEtr = Entry(frm)
    descEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="recordno:",padding=10).grid(column=0, row=2)
    rnoEtr = Entry(frm)
    rnoEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="patient id:",padding=10).grid(column=0, row=3)
    patdEtr = Entry(frm)
    patdEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="appointment:",padding=10).grid(column=0, row=4)
    appEtr = Entry(frm)
    appEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="Pid:",padding=10).grid(column=0, row=5)
    mrpidEtr = Entry(frm)
    mrpidEtr.grid(column = 1, row = 5)

   
    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=6)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=6)

    window.mainloop()