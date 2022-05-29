from asyncio.windows_events import NULL
import cx_Oracle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connection
import viewAll

def selectData(tabName,idName,id):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from {} where {} = {}'.format(tabName,idName,id))
    lst = cur.fetchone()
    conn.commit()
    conn.close()
    return lst

def updatehos(hosp_id,name,city,specialization,branch):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        update hospital set name = :nam, city = :cit,specialization =:spec, branch=:bran
        where hosp_id = :hos_id""",
        nam=name, cit=city, spec=specialization, bran= branch, hos_id=hosp_id)
    conn.commit()
    conn.close()

def updatedoc(doc_id,name,address,blood_group,dob,hosp_id):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update doctor set  name = :nam, address= :addr,blood_group =:bg,dob=:db,hosp_id=:hospid
    where doc_id = :docid""",
    docid=doc_id , nam=name, addr=address, bg=blood_group,db=dob,hospid=hosp_id)
    conn.commit()
    conn.close()

def updateroom(room_id,period,room_type,price,no_of_alloted_patients,hosp_id):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update rooms set period = :peri, room_type= :pho, price = :mai, no_of_alloted_patients = :s,hosp_id=:hospid
    where room_id = :id""",
    id=room_id, peri=period, pho=room_type, mai=price, s=no_of_alloted_patients,hospid=hosp_id)
    conn.commit()
    conn.close()

def updatepatient(pid,name,contact_no,address,sex,date_admitted,date_discharged,doc_id,room_id):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update patient set  name = :comp, contact_no = :addre, address = :mai,sex=:s,date_admitted=:da,date_discharged=:dd,doc_id=:docid,room_id=:roomid
    where  pid= :id""",
    id=pid, addre=contact_no, comp=name, mai=address,s=sex,da=date_admitted,dd=date_discharged,docid=doc_id,roomid=room_id)
    conn.commit()
    conn.close()

def updatemedical_record(blood_group,description,record_no,patient_no,appointment,pid):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        update cloth set blood_group = :type, description = :siz, record_no= :cate, patient_no = :comp, appointment = :price, pid = :cus
        where record_no = :no""",
        no=record_no, type=blood_group, siz=description, cate=record_no, comp=patient_no, price=appointment, cus=pid)
    conn.commit()
    conn.close()
