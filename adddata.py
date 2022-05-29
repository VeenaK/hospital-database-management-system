import cx_Oracle

def addpatient(pid,name,contact_no,address,sex,date_admitted,date_discharged,doc_id,room_id):
    # print(pid + " " + name + " " +contact_no+" "+address + " " +sex + " " + date_admitted + " " +date_discharged + " " +doc_id + " " + room_id)
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        insert into patient(pid, name, contact_no,address, sex, date_admitted, date_discharged, doc_id, room_id) 
        values (:patpid,:nam,:contact_nor,:addre,:s,:da,:dd,:doc_idr,:room_idr)""",
        patpid=pid, nam=name, contact_nor=contact_no,addre=address, s=sex, da=date_admitted, dd=date_discharged, doc_idr=doc_id, room_idr=room_id)
    conn.commit()
    conn.close()

def adddoctor(doc_id,name,address,blood_group,dob,hosp_id):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into doctor (doc_id,name,address,blood_group,dob,hosp_id)
    values (:docid,:nam,:addr,:bloodgroup,:dof,:hosid)""",
    docid=doc_id, nam=name,addr=address, bloodgroup=blood_group,dof=dob,hosid=hosp_id)
    conn.commit()
    conn.close()

def addrooms(room_id,period, room_type, price, no_of_alloted_patients,hosp_id):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into rooms (room_id,period, room_type, price, no_of_alloted_patients,hosp_id)
    values (:roomid, :peri, :rtype, :price, :nofallpat, :hosid)""",
    roomid=room_id, peri=period, rtype=room_type, price=price, nofallpat=no_of_alloted_patients,hosid=hosp_id)
    conn.commit()
    conn.close()

def addhospital(hosp_id,name, city, specialization, branch):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into hospital (hosp_id,name, city, specialization, branch)
    values (:hosid, :name, :city, :spec,:branch)""",
    hosid=hosp_id, name=name, city=city, spec=specialization, branch=branch)
    conn.commit()
    conn.close()

def addmedical_record(blood_group, description, record_no, patient_no, appointment, pid):
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into medical_record (blood_group, description, record_no, patient_no, appointment, pid)
    values (:bg, :des, :rno, :pno,:appt, :pidr)""",
    bg=blood_group,des=description, rno=record_no, pno=patient_no, appt=appointment,pidr=pid)
    conn.commit()
    conn.close()