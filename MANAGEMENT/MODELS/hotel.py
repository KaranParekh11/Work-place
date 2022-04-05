import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/UTILS')
from test1 import engine, conn, metadata, db, inspector,Hotel
from sqlalchemy import Table, Column, Integer, String 

def insert_hotel_info(dicth):
    hotel_id=dicth["Hotel_id"]
    hotel_name=dicth["Hotel_name"]
    star=dicth["Star"]
    distance=dicth["Distance"]
    time=dicth['Time']
    ins = db.insert(Hotel).values(Hotel_Id=hotel_id,Hotel_name=hotel_name,Star=star,Distance=distance,Time=time)
    conn.execute(ins)

def delete_hotel_info(id):
    try:
        query1 = Hotel.select().where(Hotel.c.Hotel_Id == id)
        result = conn.execute(query1)
        row2 = result.fetchone()
        if row2!=None:
            query2 = Hotel.delete().where(Hotel.c.Hotel_Id == id)
            conn.execute(query2)
            return "success"
        else:
            return "error"
    except:
        return "error"

def update_hotel_info(id,ndicth):
    query1 = Hotel.select()
    result = conn.execute(query1)
    li=list(result._metadata.keys)
    # print(li)
    for (key,value) in ndicth.items():
        # print(key)
        if key in li:
            try:
                query1 = Hotel.select().where(Hotel.c.Hotel_Id == id)
                result = conn.execute(query1)
                row2 = result.fetchone()
                if row2!=None:
                    ins = db.update(Hotel).values({key : value}).where(Hotel.c.Hotel_Id == id)
                    conn.execute(ins)
                    x="success"
                else:
                    x="enter valid hotel id!!!"
            except:
                x="error"
        
        else:
            x="enter valid data for update!!!"
    return x

def get_all_hotel_info():
    result = conn.execute("SELECT Hotel.Hotel_Id, Hotel_name, Star, Distance, Time, Dish_name, Price FROM Dishes INNER JOIN Hotel ON Hotel.Hotel_Id = Dishes.Hotel_Id")
    rows=result.fetchall()
    # print(rows)
    dict10={
        "Hotels":[]
    }
    l2=[]
    k=0
    t=0
    for i in rows:
        if k==0:
            dict50={}
            dict50["Hotel_name"]=i[1]
            temp=i[1]
            # print(temp)
            dict50["Star"]=i[2]
            dict50["Distance"]=i[3]
            dict50["Time"]=i[4]
            dict50["Dishes"]={i[5]:i[6]}
            l2.append(dict50)
            # rc=rc-1
            k=1
            t=t+1
        else:
            if temp==i[1]:
                dict25={i[5]:i[6]}
                dict26=l2[t-1]
                dict27=dict26["Dishes"]
                l2.pop(t-1)
                dict27.update(dict25)
                l2.append(dict26)
                # print(dict26)
            else:
                k=0     
    dict10["Hotels"]=l2
    return dict10
