from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import up
import updatedata
import viewAll


# Update hospital
def updatehosUi(id):
    def cancelBtn():
        window.destroy()
        viewAll.viewhos()

    def updateBtn():
        if(hosidEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee ID cannot be Empty')
        else:
           hos_id = hosidEtr.get()
        if(hosnameEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee Name cannot be Empty')
        else:
            empName = hosnameEtr.get()
        if(cityEtr.get() == ''):
            address = ''
        else:
            address = cityEtr.get()
        if(specEtr.get() == ''):
            sex = ''
        else:
            sex = specEtr.get()
        if(brancEtr.get() == ''):
            salary = ''
        else:
            salary = brancEtr.get()
       
        
        # print(empId + " " + empName + " " +address + " " +sex + " " + salary + " " +phoneNo + " " +mgrId + " " + secNo)
        # print(type(salary))

        updatedata.updatehos(hos_id,empName,address,sex, salary)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewhos()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update hospital")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updatedata.selectData('hospital', 'hosp_id', id)

    # Fields
    ttk.Label(frm, text="hospital ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    hosidEtr = Entry(frm)
    hosidEtr.insert(0,str(lst[0]))
    # empIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="hospital Name:",padding=10).grid(column=0, row=1)
    hosnameEtr = Entry(frm)
    hosnameEtr.insert(0,str(lst[1]))
    hosnameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="city:",padding=10).grid(column=0, row=2)
    cityEtr = Entry(frm)
    cityEtr.insert(0,str(lst[2]))
    cityEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="specialization:",padding=10).grid(column=0, row=3)
    specEtr = Entry(frm)
    specEtr.insert(0,str(lst[3]))
    specEtr.grid(column = 1, row = 3 )

    ttk.Label(frm, text="branch:",padding=10).grid(column=0, row=4)
    brancEtr = Entry(frm)
    brancEtr.insert(0,str(lst[4]))
    brancEtr.grid(column = 1, row = 4)


    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=8)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=8)

    window.mainloop()

# Update doctor
def updateSecUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewdoc()

    def updateBtn():

        if(docidEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='doc id cannot be Empty')
        else:
            secNo = docidEtr.get()
        
        if(docnameEtr.get() == ''):
            secName = ''
        else:
            secName = docnameEtr.get()
        
        if(docaddrEtr.get() == ''):
            secLoc = ''
        else:
            secLoc = docaddrEtr.get()
        
        if(bgEtr.get() == ''):
            mgrId = ''
        else:
            mgrId = bgEtr.get()
        
        if(dobEtr.get() == ''):
           dob = ''
        else:
           dob =dobEtr.get()
        
         
        if(idEtr.get() == ''):
           hosid = ''
        else:
           hosid=idEtr.get()
        

        updatedata.updatedoc(secNo,secName,secLoc,mgrId,dob,hosid)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewdoc()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update doctor")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updatedata.selectData('doctor', 'doc_id', id)

    # Fields
    ttk.Label(frm, text="doc id:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    docidEtr = Entry(frm)
    docidEtr.insert(0,str(lst[0]))
    # secNoEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="doc Name:",padding=10).grid(column=0, row=1)
    docnameEtr = Entry(frm)
    docnameEtr.insert(0,str(lst[1]))
    docnameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="doc addr:",padding=10).grid(column=0, row=2)
    docaddrEtr = Entry(frm)
    docaddrEtr.insert(0,str(lst[2]))
    docaddrEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="blood group:",padding=10).grid(column=0, row=3)
    bgEtr = Entry(frm)
    bgEtr.insert(0,str(lst[3]))
    bgEtr.grid(column = 1, row = 3)

    
    ttk.Label(frm, text="dob:",padding=10).grid(column=0, row=4)
    dobEtr = Entry(frm)
    dobEtr.insert(0,str(lst[4]))
    dobEtr.grid(column = 1, row = 4)
    
    
    ttk.Label(frm, text="hosp_id:",padding=10).grid(column=0, row=5)
    idEtr = Entry(frm)
    idEtr.insert(0,str(lst[5]))
    idEtr.grid(column = 1, row = 5)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=6)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=6)

    window.mainloop()

# Update rooms
def updateCusUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewrooms()

    def updateBtn():

        if(roomIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='room ID cannot be Empty')
        else:
            cusId =roomIdEtr.get()
        if(periEtr.get() == ''):
            cusName = ''
        else:
            cusName = periEtr.get()
        if(rtEtr.get() == ''):
            phoneNo = ''
        else:
            phoneNo = rtEtr.get()
        if(priceEtr.get() == ''):
            mail = ''
        else:
            mail = priceEtr.get()
        if(nalEtr.get() == ''):
            sex = ''
        else:
            sex = nalEtr.get()
        if(idEtr.get() == ''):
           hid = ''
        else:
           hid = idEtr.get()
    

        updatedata.updateroom(cusId, cusName, phoneNo, mail, sex,hid)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewrooms()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update rooms")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updatedata.selectData('rooms', 'room_id', id)

    # Fields
    ttk.Label(frm, text="room ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    roomIdEtr = Entry(frm)
    roomIdEtr.insert(0,str(lst[0]))
    # cusIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="period:",padding=10).grid(column=0, row=1)
    periEtr = Entry(frm)
    periEtr.insert(0,str(lst[1]))
    periEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="room type:",padding=10).grid(column=0, row=2)
    rtEtr = Entry(frm)
    rtEtr.insert(0,lst[2])
    rtEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="price:",padding=10).grid(column=0, row=3)
    priceEtr = Entry(frm)
    priceEtr.insert(0,str(lst[3]))
    priceEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="no of all pat:",padding=10).grid(column=0, row=4)
    nalEtr = Entry(frm)
    nalEtr.insert(0,str(lst[4]))
    nalEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="hos id:",padding=10).grid(column=0, row=5)
    idEtr = Entry(frm)
    idEtr.insert(0,str(lst[5]))
    idEtr.grid(column = 1, row = 5)
    
    
    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=6)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=6)

    window.mainloop()

# Update patient
def updateSupUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewpat()

    def updateBtn():
        if(pidEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='patient ID cannot be Empty')
        else:
            supId = pidEtr.get()
        if(nameEtr.get() == ''):
            phoneNo = ''
        else:
            phoneNo = nameEtr.get()
        if(comEtr.get() == ''):
            company = ''
        else:
            company = comEtr.get()
        if(addressEtr.get() == ''):
            address = ''
        else:
            address = addressEtr.get()
        if(sexEtr.get() == ''):
            mail = ''
        else:
            mail =sexEtr.get()
        if(admEtr.get() == ''):
           ad = ''
        else:
            ad =admEtr.get()
        if(ddEtr.get() == ''):
           dd = ''
        else:
            dd =ddEtr.get()
        if(diEtr.get() == ''):
          di = ''
        else:
            di =diEtr.get()
        if(idEtr.get() == ''):
           id = ''
        else:
          id =idEtr.get()

        updatedata.updatepatient(supId, phoneNo, company, address, mail,ad,dd,di,id)

        messagebox.showinfo(title="Update",message="1 Row Updated")
        window.destroy()
        viewAll.viewpat()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update patient")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updatedata.selectData('patient', 'pid', id)

    # Fields
    ttk.Label(frm, text="patient ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    pidEtr = Entry(frm)
    pidEtr.insert(0,str(lst[0]))
    # supIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="name:",padding=10).grid(column=0, row=1)
    nameEtr = Entry(frm)
    nameEtr.insert(0,str(lst[1]))
    nameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Contact no:",padding=10).grid(column=0, row=2)
    comEtr = Entry(frm)
    comEtr.insert(0,str(lst[2]))
    comEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Address:",padding=10).grid(column=0, row=3)
    addressEtr = Entry(frm)
    addressEtr.insert(0,str(lst[3]))
    addressEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="sex:",padding=10).grid(column=0, row=4)
    sexEtr = Entry(frm)
    sexEtr.insert(0,str(lst[4]))
    sexEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="date admitted:",padding=10).grid(column=0, row=5)
    admEtr = Entry(frm)
    admEtr.insert(0,str(lst[5]))
    admEtr.grid(column = 1, row = 5)

    ttk.Label(frm, text="date discharged:",padding=10).grid(column=0, row=6)
    ddEtr = Entry(frm)
    ddEtr.insert(0,str(lst[6]))
    ddEtr.grid(column = 1, row = 6)

    ttk.Label(frm, text="doc id:",padding=10).grid(column=0, row=7)
    diEtr = Entry(frm)
    diEtr.insert(0,str(lst[7]))
    diEtr.grid(column = 1, row = 7)

    ttk.Label(frm, text="room id:",padding=10).grid(column=0, row=8)
    idEtr = Entry(frm)
    idEtr.insert(0,str(lst[8]))
    idEtr.grid(column = 1, row = 8)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=9)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=9)


    window.mainloop()

# Update medical record
def updateCloUi(id):
    def cancelBtn():
        window.destroy()
        viewAll.viewmr()

    def updateBtn():
        if(rNoEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='record no cannot be Empty')
        else:
            cloNo = rNoEtr.get()
        if(bTypeEtr.get() == ''):
            cloType = ''
        else:
            cloType = bTypeEtr.get()
        if(descSizeEtr.get() == ''):
            cloSize = ''
        else:
            cloSize = descSizeEtr.get()
        if(pateEtr.get() == ''):
            category = ''
        else:
            category = pateEtr.get()
        if(apptEtr.get() == ''):
            company = ''
        else:
            company = apptEtr.get()
        if(priEtr.get() == ''):
            price = ''
        else:
            price = priEtr.get()


        updatedata.updatemedical_record(cloNo, cloType, cloSize, category, company, price)

        messagebox.showinfo(title="Update",message="1 Row Updated")
        window.destroy()
        viewAll.viewmr()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update mr")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updatedata.selectData('medical_record', 'record_no', id)

    # Fields
    ttk.Label(frm, text="record No:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    rNoEtr = Entry(frm)
    rNoEtr.insert(0,str(lst[0]))
    # cloNoEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="blood group:",padding=10).grid(column=0, row=1)
    bTypeEtr = Entry(frm)
    bTypeEtr.insert(0,str(lst[1]))
    bTypeEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="description:",padding=10).grid(column=0, row=2)
    descSizeEtr = Entry(frm)
    descSizeEtr.insert(0,str(lst[2]))
    descSizeEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="patient no:",padding=10).grid(column=0, row=3)
    pateEtr = Entry(frm)
    pateEtr.insert(0,str(lst[3]))
    pateEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="appointment:",padding=10).grid(column=0, row=4)
    apptEtr = Entry(frm)
    apptEtr.insert(0,str(lst[4]))
    apptEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="pid:",padding=10).grid(column=0, row=5)
    priEtr = Entry(frm)
    priEtr.insert(0,str(lst[5]))
    priEtr.grid(column = 1, row = 5)

    
    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=9)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=9)

    window.mainloop()


# Dialog Boxes
def updateHosDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updatedata.selectData('hospital', 'hosp_id' , id) != None):
                window.destroy()
                updatehosUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewhos()

    window = Tk()
    window.title("Update hospiatal")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter hospital ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updateDocDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updatedata.selectData('doctor', 'doc_id' , id) != None):
                window.destroy()
                updateSecUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewdoc()

    window = Tk()
    window.title("Update doctor")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter doc id to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()


def updateRoomDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updatedata.selectData('rooms', 'room_id' , id) != None):
                window.destroy()
                updateCusUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewrooms()

    window = Tk()
    window.title("Update rooms")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter room ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updatePatDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updatedata.selectData('patient', 'pid' , id) != None):
                window.destroy()
                updateSupUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewpat()

    window = Tk()
    window.title("Update patient")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter pat ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updateMedDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updatedata.selectData('medical_record', 'record_no' , id) != None):
                window.destroy()
                updateCloUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewmr()

    window = Tk()
    window.title("Update mr")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter rNo to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()
