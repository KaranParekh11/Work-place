import sqlite3
from flask import jsonify

con=sqlite3.connect("app.db",check_same_thread=False)
cur=con.cursor()

def create_database_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS Hotel(hotel_id TEXT PRIMARY KEY,hotel_name TEXT,Star INTEGER,Distance TEXT,time TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS Dishes(dish_id TEXT PRIMARY KEY,dish_name TEXT,price INTEGER,hotel_id TEXT,FOREIGN KEY(hotel_id) REFERENCES Hotel(hotel_id))")

    cur.execute("CREATE TABLE IF NOT EXISTS User(user_id TEXT PRIMARY KEY,name TEXT,email TEXT,dob TEXT,salt TEXT,digest TEXT,refresh_token TEXT)")
  
def insert_user_info(data1):
    user_id=data1["user_id"]
    name=data1["name"]
    email=data1["email"]
    dob=data1["dob"]
    salt=data1['salt']
    digest=data1['digest']
    cur.execute("INSERT INTO User VALUES (?, ?, ?, ?, ?, ?, NULL)", (user_id, name, email, dob, salt, digest))
    con.commit()
    # cur.execute("SELECT * FROM User")
    # rows=cur.fetchall()
    # for row in rows:
    #     print(row)
    
def get_email(email):
    query=f"SELECT email FROM User WHERE email LIKE '"'{}'"'".format(email)
    try:
        cur.execute(query)
        row=cur.fetchone()
        if row[0]==email:
            x=True
        else:
            x=False
    except:
        x=False
    return x

def insert_token(email,token):
    query = f"UPDATE User SET refresh_token = '"'{}'"' WHERE email LIKE '"'{}'"'".format(token,email)
    # print(query)
    cur.execute(query)
    con.commit()
    # query1=f"SELECT * FROM User WHERE email LIKE '"'{}'"'".format(email)
    # cur.execute(query1)
    # rows=cur.fetchone()
    # for i in rows:
    #     print(i)
    
def get_password(email,password):
    query=f"SELECT * FROM User WHERE email LIKE '"'{}'"'".format(email)
    cur.execute(query)
    rows=cur.fetchone()
    user_id=rows[0]
    salt=rows[4]
    digest=rows[5]
    return user_id,salt,digest

def view_data():
    cur.execute("SELECT * FROM User")
    rows=cur.fetchall()
    # for row in rows:
    #     print(row)
    return jsonify(rows)

def update_user_table(key,value,id):
    try:
        # print(key,value)
        query = f"UPDATE User SET '"'{}'"' = '"'{}'"' WHERE user_id LIKE '"'{}'"'".format(key,value,id)
        cur.execute(query)
        con.commit()
        query1=f"SELECT * FROM User WHERE user_id LIKE '"'{}'"'".format(id)
        cur.execute(query1)
        rows=cur.fetchone()
        if rows!=None:
            return "success"
        else:
            return "error1"
    except:
        return "error2"

def delete_user_info(id):
    try:
        query1=f"SELECT * FROM User WHERE user_id LIKE '"'{}'"'".format(id)
        cur.execute(query1)
        row2=cur.fetchone()
        query = f"DELETE FROM User WHERE user_id LIKE '"'{}'"'".format(id)
        cur.execute(query)
        row1=cur.fetchone()
        con.commit()
        if row2!=None:
            return "success"
        else:
            return "error"
    except:
        return "error"
    
def get_data_by_id(id):
    try:
        query1=f"SELECT * FROM User WHERE user_id LIKE '"'{}'"'".format(id)
        cur.execute(query1)
        row2=cur.fetchone()
        if row2!=None:
            return row2
        else:
            return "error"
    except:
        return "error"

def aces_token(id):
    try:
        query1=f"SELECT email FROM User WHERE user_id LIKE '"'{}'"'".format(id)
        cur.execute(query1)
        row2=cur.fetchone()
        print(row2)
        if row2!=None:
            return row2
        else:
            return "error"
    except:
        return "error"

def insert_hotel_info(dicth):
    hotel_id=dicth["Hotel_id"]
    hotel_name=dicth["Hotel_name"]
    star=dicth["Star"]
    distance=dicth["Distance"]
    time=dicth['Time']
    cur.execute("INSERT INTO Hotel VALUES (?, ?, ?, ?, ?)", (hotel_id, hotel_name, star, distance, time))
    con.commit()

def insert_Dish_info(dish_list):
    for i in dish_list:
        Dish_id=i["Dish_id"]
        Dish_name=i["Dish_name"]
        price=i["Price"]
        hotel_id=i["Hotel_id"]
        cur.execute("INSERT INTO Dishes VALUES (?, ?, ?, ?)", (Dish_id, Dish_name, price, hotel_id))
        con.commit()

def delete_hotel_info(id):
    try:
        query1=f"SELECT * FROM Hotel WHERE hotel_id LIKE '"'{}'"'".format(id)
        cur.execute(query1)
        row2=cur.fetchone()
        query = f"DELETE FROM Hotel WHERE hotel_id LIKE '"'{}'"'".format(id)
        cur.execute(query)
        row1=cur.fetchone()
        con.commit()
        if row2!=None:
            return "success"
        else:
            return "error"
    except:
        return "error"

def delete_dish_info(id):
    try:
        query1=f"SELECT * FROM Dishes WHERE hotel_id LIKE '"'{}'"'".format(id)
        cur.execute(query1)
        row2=cur.fetchone()
        query = f"DELETE FROM Dishes WHERE hotel_id LIKE '"'{}'"'".format(id)
        cur.execute(query)
        row1=cur.fetchone()
        con.commit()
        if row2!=None:
            return "success"
        else:
            return "error"
    except:
        return "error"

def update_Dish_info(id,ndish_list):
    # print(ndish_list)
    try:
        query1=f"SELECT * FROM Dishes WHERE hotel_id LIKE '"'{}'"'".format(id)
        cur.execute(query1)
        rows=cur.fetchall()
        if rows!=None:
            for i in ndish_list:
                Dish_name=i["Dish_name"]
                Price=i["Price"]
                # print(Dish_name,Price)
                query = f"UPDATE Dishes SET price = '"'{}'"' WHERE hotel_id LIKE '"'{}'"' AND dish_name LIKE '"'{}'"'".format(Price,id,Dish_name)
                cur.execute(query)
                rows=cur.fetchall()
                # print(rows)
                con.commit()
            return "hotel info updated successfully!!!"
        else:
            return "enter valid hotel id!!!"
    except:
        return "error"
            
def update_hotel_info(id,ndicth):
    abc=cur.execute("SELECT * FROM Hotel ")
    li=[]
    for column in abc.description:
        li.append(column[0].capitalize())
    print(li)
    for (key,value) in ndicth.items():
        print(key)
        if key in li:
            try:
                query1=f"SELECT * FROM Hotel WHERE hotel_id LIKE '"'{}'"'".format(id)
                cur.execute(query1)
                rows=cur.fetchone()
                if rows!=None:
                    query = f"UPDATE Hotel SET '"'{}'"' = '"'{}'"' WHERE hotel_id LIKE '"'{}'"'".format(key,value,id)
                    cur.execute(query)
                    con.commit()
                    query = f"SELECT * FROM Hotel WHERE hotel_id LIKE '"'{}'"'".format(key,value,id)
                    cur.execute(query)
                    rows=cur.fetchone()
                    print(rows)
                    x="hotel info updated successfully!!!"
                else:
                    x="enter valid hotel id!!!"
            except:
                x="error"
        
        else:
            x="enter valid data for update!!!"
    return x
        
def get_all_hotel_info():
    cur.execute("SELECT Hotel.hotel_id, hotel_name, star, distance, time, dish_name, price FROM Dishes INNER JOIN Hotel ON Hotel.hotel_id = Dishes.hotel_id")
    rows=cur.fetchall()
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

