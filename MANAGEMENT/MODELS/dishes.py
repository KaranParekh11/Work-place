import sys
import uuid
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/UTILS')
from test1 import engine, conn, metadata, db, inspector,Dishes
from sqlalchemy import Table, Column, Integer, String, ForeignKey, and_


def insert_Dish_info(dish_list):
    for i in dish_list:
        Dish_id=i["Dish_id"]
        Dish_name=i["Dish_name"]
        price=i["Price"]
        hotel_id=i["Hotel_id"]
        ins = db.insert(Dishes).values(Hotel_Id=hotel_id,Dish_name=Dish_name,Price=price,Dish_Id=Dish_id)
        conn.execute(ins)
    query1 = Dishes.select().where(Dishes.c.Hotel_Id == hotel_id)
    result = conn.execute(query1)
    row2 = result.fetchone()
    return row2[0]


def delete_dish_info(id):
    try:
        query1 = Dishes.select().where(Dishes.c.Dish_Id == id)
        result = conn.execute(query1)
        row2 = result.fetchone()
        if row2!=None:
            query2 = Dishes.delete().where(Dishes.c.Dish_Id == id)
            conn.execute(query2)
            return "success"
        else:
            return "error"
    except:
        return "error"

def update_Dish_info(ndish_dict):
    name=ndish_dict["Dish_name"]
    price=ndish_dict["Price"]
    id= ndish_dict["Dish_Id"]
    try:
        query1 = Dishes.select().where(Dishes.c.Dish_Id == id)
        result = conn.execute(query1)
        row2 = result.fetchone()
        if row2!=None:
            ins = db.update(Dishes).values({ Dishes.c.Dish_name : name, Dishes.c.Price :price}).where(Dishes.c.Dish_Id == id)
            conn.execute(ins)
            return "success"
        else:
            return "Enter valid dish id for updating!!!"
    except:
        return "ERROR"
   
def get_all_dish_info():
    result = conn.execute("SELECT Hotel.Hotel_Id, Hotel_name, Dish_name, Price FROM Dishes INNER JOIN Hotel ON Hotel.Hotel_Id = Dishes.Hotel_Id")
    rows=result.fetchall()
    for i in rows:
        print(i)
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
            dict50["Dishes"]={i[2]:i[3]}
            l2.append(dict50)
            k=1
            t=t+1
        else:
            if temp==i[1]:
                dict25={i[2]:i[3]}
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