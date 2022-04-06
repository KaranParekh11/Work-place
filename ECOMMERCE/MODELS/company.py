import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
from test1 import engine, conn, metadata, db, inspector, company
from sqlalchemy import Table, Column, Integer, String , and_ 


def insert_company_info(dicth):

    name=dicth["name"]
    id = dicth["id"]
    category=dicth["category"]
    website=dicth["website"]
    days=dicth['days']
    time=dicth['time']
    address=dicth['address']
    ins = db.insert(company).values(id=id,name=name,category=category,website=website,days=days,time=time,address=address)
    conn.execute(ins)

def delete_company_info(id):
    
    query1 = company.select().where(company.c.id == id)
    result = conn.execute(query1)
    row2 = result.fetchone()
    if row2!=None:
        query2 = company.delete().where(company.c.id == id)
        conn.execute(query2)
        return "success"
    else:
        return "error"
    

def update_company_info(id,ndicth):
    query1 = company.select()
    result = conn.execute(query1)
    li=list(result._metadata.keys)
    # print(li)
    for (key,value) in ndicth.items():
        # print(key)
        if key in li:
            query1 = company.select().where(company.c.id == id)
            result = conn.execute(query1)
            row2 = result.fetchone()
            if row2!=None:
                ins = db.update(company).values({key : value}).where(company.c.id == id)
                conn.execute(ins)
                x = "success"
            else:
                x = "enter valid hotel id!!!"
        else:
            x = "enter valid data for update!!!"
    return x

def get_data_by_id(id):
    query1 = company.select().where(company.c.id == id)
    result = conn.execute(query1)
    rows = result.fetchone()
    if rows!=None:
        return rows
    else:
        return "error" 


def search_company(search_dict):
    l=[]
    for key in search_dict.items():
        l.append(key)
    count=len(l)
    p=1
    # print(count)
    query1="SELECT * FROM company WHERE "
    valuedict={} 
    for key,value in search_dict.items():
        if p<count:
            str1 = "company."+key+"=:value"+str(p)+" AND " 
            query1 = query1+str1    
        else:
            str1 =  "company."+key+"=:value"+str(p)
            query1 = query1 + str1 
        valuedict["value"+str(p)]=value   
        p=p+1
            
    # print(valuedict)
    # print(query1)
    result = conn.execute(query1,valuedict)
    rows = result.fetchall()
    # print(rows)
    return rows
        

    
def get_all_company_info():
    result = conn.execute("SELECT company.id, company.name, website, category, time, days,address,product.name, price FROM product INNER JOIN company ON company.id = product.company_id")
    rows=result.fetchall()
    # print(rows)
    # for i in rows:
    #     print(i)
    l2=[]
    k=0
    t=0
    for i in rows:
        if k==0:
            dict50={}
            temp=0
            dict50["name"]=i[1]
            temp=i[1]
            # print(temp)
            dict50["website"]=i[2]
            dict50["category"]=i[3]
            dict50["time"]=i[4]
            dict50["days"]=i[5]
            dict50["address"]=i[6]
            dict50["products"]={i[7]:i[8]}
            l2.append(dict50)
            # rc=rc-1
            k=1
            t=t+1
        else:
            if temp==i[1]:
                dict25={i[7]:i[8]}
                dict26=l2[t-1]
                dict27=dict26["products"]
                l2.pop(t-1)
                dict27.update(dict25)
                l2.append(dict26)
                # print(dict26)
            else:
                k=0   
    dict10={}  
    dict10["companies"]=l2
    return dict10
    
