import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
from test1 import engine, conn, metadata, db, inspector,create_database_tabels,user
from sqlalchemy import Table, Column, Integer, String,Date
from datetime import datetime as dt

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
        dob=dt.strptime(dob1,"%d-%m-%Y")
    except:
        dob=dt.strptime(dob1,"%d/%m/%Y")
    salt=data['salt']
    digest=data['digest']
    ins = db.insert(user).values(id=id,name=name,email=email,mobileno=mobile,dob=dob,salt=salt,digest=digest)
    conn.execute(ins)

def get_email(email):
    query = user.select().where(user.c.email == email)
    try:
        result = conn.execute(query)
        row = result.fetchone()
        # print(row)
        if row[2]==email:
            x=True
        else:
            x=False
    except:
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

def insert_token(email,token):
    ins = db.update(user).values(refresh_Token=token).where(user.c.email == email)
    conn.execute(ins)

def update_user_table(key,value,id):
    query = user.select().where(user.c.id == id)
    result = conn.execute(query)
    rows = result.fetchone()
    ins = db.update(user).values({key : value}).where(user.c.id == id)
    conn.execute(ins)
    if rows!=None:
        return "success"
    else:
        return "error1"
    
def get_data_by_id(id):
    query1 = user.select().where(user.c.id == id)
    result = conn.execute(query1)
    rows = result.fetchone()
    if rows!=None:
        return rows
    else:
        return "error" 
    

def aces_token(id):
    query1 = user.select().where(user.c.id == id)
    result = conn.execute(query1)
    rows = result.fetchone()
    # print(rows)
    if rows!=None:
        return rows[2]
    else:
        return "error" 
   

def delete_user_info(id):
    query1 = user.select().where(user.c.id == id)
    result = conn.execute(query1)
    row2 = result.fetchone()
    if row2!=None:
        query1 = user.delete().where(user.c.id == id)
        conn.execute(query1)
        return "success"
    else:
        return "error"



