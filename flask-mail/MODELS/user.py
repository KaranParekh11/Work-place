import sys
sys.path.insert(0,'E:/KARAN PY/flask-mail/UTILS')
from dbcreate import engine, conn, metadata, db, inspector,create_database_tabels,user
from sqlalchemy import Table, Column, Integer, String,Date,and_
import datetime as dt

def insert_user_info(data1):
    data={}
    for key,value in data1.items():
        key=key.lower()
        data[key]=value
    # print(data)
    id=data["id"]
    name=data["name"]
    email=data["email"]
    mobile=data["mobileno"]
    dob1=data["dob"]
    try:
        dob=dt.datetime.strptime(dob1,"%d-%m-%Y")
    except:
        dob=dt.datetime.strptime(dob1,"%d/%m/%Y")
    salt=data['salt']
    digest=data['digest']
    ins = db.insert(user).values(id=id,name=name,email=email,mobileno=mobile,dob=dob,salt=salt,digest=digest,otp=-1,isverify=bool(False))
    conn.execute(ins)

def get_email(email):
    query = user.select().where(user.c.email == email)
    result = conn.execute(query)
    row = result.fetchone()
    # print(row)
    if row!=None:
        x=True
    else:
        x=False
    return x

def get_password(email,password):
    query = user.select().where(user.c.email == email)
    result = conn.execute(query)
    rows = result.fetchone()
    id=rows[0]
    salt=rows[5]
    digest=rows[6]
    return id,salt,digest


def isverify1(email):
    query1 = user.select().where(and_(user.c.isverify == bool(False),user.c.email == email))   
    result1 = conn.execute(query1)
    row1 = result1.fetchone()
    if row1!=None:
        if row1[9] == False:
            return "success"
    else:
        return "verified"


def insertotp(email,otp):
    ins = db.update(user).values(otp=otp,expire_at=dt.datetime.now()).where(user.c.email == email)
    conn.execute(ins)
    # ins1 = db.insert(user).values(expire_at=dt.datetime.now()).where(user.c.email == email)
    # conn.execute(ins1)
def verified(email,otp,time):
    query1 = user.select().where(and_(user.c.otp == otp,user.c.email == email))
    result1 = conn.execute(query1)
    row1 = result1.fetchone()
    if row1!=None:
        query2 = user.select().where(and_(user.c.otp == otp,user.c.email == email))
        result2 = conn.execute(query2)
        row2 = result2.fetchone()
        z1=row2[8]
        if time-z1 <= dt.timedelta(seconds=30):
            ins = db.update(user).values(isverify=bool(True)).where(user.c.email == email)
            conn.execute(ins)
            return "success"
        else:
            return "failure"
    else:
        return "error" 


        
def isaccverified(email):
    query1 = user.select().where(and_(user.c.isverify == bool(True),user.c.email == email))   
    result1 = conn.execute(query1)
    row1 = result1.fetchone()
    if row1!=None:
        return "verified"
    else:
        return "failure"

    
def forreset(email,otp,np,z,salt,digest):
    query1 = user.select().where(and_(user.c.otp == otp,user.c.email == email))
    result1 = conn.execute(query1)
    row1 = result1.fetchone()
    if row1!=None:
        query2 = user.select().where(and_(user.c.otp == otp,user.c.email == email))
        result2 = conn.execute(query2)
        row2 = result2.fetchone()
        z1=row2[8]
        if z-z1 <= dt.timedelta(seconds=30):
            ins = db.update(user).values(salt=salt,digest=digest).where(user.c.email == email)
            conn.execute(ins)
            return "success"
        else:
            return "failure"
    else:
        return "error" 
