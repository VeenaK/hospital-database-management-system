from unicodedata import name
import cx_Oracle
import sys

#create connection

try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:/Users/vinay/OneDrive/Documents/instantclient-basic-windows.x64-21.3.0.0.0 (2)/instantclient_21_3")
except Exception as err:
    print("Whoops!")
    print(err)
    sys.exit(1)

# conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
# print(conn.version)
#create cursor

# cur = conn.cursor()


def hosLst():
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from hospital")
    hosLst = cur.fetchall()
    return hosLst

def patLst():
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from patient")
    patLst = cur.fetchall()
    return patLst

def docLst():
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from doctor")
    docLst = cur.fetchall()
    return docLst

def roomLst():
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from rooms")
    roomLst = cur.fetchall()
    return roomLst

def mrLst():
    conn = cx_Oracle.connect('veena/8431258285@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from medical_record")
    mrLst = cur.fetchall()
    return mrLst











# conn.commit()
# conn.close()