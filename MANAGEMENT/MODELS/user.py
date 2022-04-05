import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/UTILS')
from test1 import engine, conn, metadata, db, inspector,create_database_tabels,User
from sqlalchemy import Table, Column, Integer, String

def insert_user_info(data1):
    user_id=data1["user_id"]
    name=data1["name"]
    email=data1["email"]
    dob=data1["dob"]
    salt=data1['salt']
    digest=data1['digest']
    ins = db.insert(User).values(User_Id=user_id,User_name=name,Email=email,DOB=dob,Salt=salt,Digest=digest)
    conn.execute(ins)

def get_email(email):
    query = User.select().where(User.c.Email == email)
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
    query = User.select().where(User.c.Email == email)
    result = conn.execute(query)
    rows = result.fetchone()
    user_id=rows[0]
    salt=rows[4]
    digest=rows[5]
    return user_id,salt,digest

def insert_token(email,token):
    ins = db.update(User).values(Refresh_Token=token).where(User.c.Email == email)
    conn.execute(ins)

def update_user_table(key,value,id):
    try:
        query = User.select().where(User.c.User_Id == id)
        result = conn.execute(query)
        rows = result.fetchone()
        ins = db.update(User).values({key : value}).where(User.c.User_Id == id)
        conn.execute(ins)
        if rows!=None:
            return "success"
        else:
            return "error1"
    except:
        return "error2"

def get_data_by_id(id):
    try:
        query1 = User.select().where(User.c.User_Id == id)
        result = conn.execute(query1)
        rows = result.fetchone()
        if rows!=None:
            return rows
        else:
            return "error" 
    except:
        return "error"

def aces_token(id):
    try:
        query1 = User.select().where(User.c.User_Id == id)
        result = conn.execute(query1)
        rows = result.fetchone()
        if rows!=None:
            return rows[2]
        else:
            return "error" 
    except:
        return "error"

def delete_user_info(id):
    try:
        query1 = User.select().where(User.c.User_Id == id)
        result = conn.execute(query1)
        row2 = result.fetchone()
        if row2!=None:
            query1 = User.delete().where(User.c.User_Id == id)
            conn.execute(query1)
            return "success"
        else:
            return "error"
    except:
        return "error"


