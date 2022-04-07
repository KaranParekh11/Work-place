import sys
import uuid
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
from test1 import engine, conn, metadata, db, inspector,product,company
from sqlalchemy import Table, Column, Integer, String, ForeignKey, and_


def insert_product_info(id,product_list):
    query1 = company.select().where(company.c.id == id)
    result = conn.execute(query1)
    rows = result.fetchone()
    if rows!=None:
        for i in product_list:
            ins = db.insert(product).values(id=i["id"],name=i["name"],price=i["price"],description=i["description"],stock=i["stock"],company_id=id)
            conn.execute(ins)
        return "success"
    else:
        return "error" 


def delete_product_info(id):
    query1 = product.select().where(product.c.id == id)
    result = conn.execute(query1)
    row2 = result.fetchone()
    if row2!=None:
        query2 = product.delete().where(product.c.id == id)
        conn.execute(query2)
        return "success"
    else:
        return "error"
    

def update_product_info(id,nproduct_dict):
    # print(nproduct_dict)
    query1 = product.select()
    result = conn.execute(query1)
    li=list(result._metadata.keys)
    query2 = product.select().where(product.c.id == id)
    result = conn.execute(query2)
    row2 = result.fetchone()
    # print(li)
    if row2!=None:
        l=[]
        for key in nproduct_dict.keys():
            
            key=key.lower()
            # print(key)
            if key in li:
                l.append(key)
            else:
                return "enter valid data for update"
        count=len(l)
        p=1
        query1="UPDATE product SET "

        valuedict={} 
        for key,value in nproduct_dict.items():
                if p<count:
                    str1 = key+"=:value"+str(p)+", " 
                    query1 = query1+str1    
                else:
                    str1 =  key+"=:value"+str(p)+" WHERE product.id =:id"
                    query1 = query1 + str1 
                valuedict["value"+str(p)]=value
                valuedict["id"]=id 
                p=p+1
        # print(valuedict)  
        conn.execute(query1,valuedict)       
        return "success"
    else:
        return "error"
    
   
def get_all_product_info():
    result = conn.execute("SELECT company.name ,product.name, price, stock ,description FROM company INNER JOIN product ON company.id = product.company_id")
    rows=result.fetchall()
    # print(rows)
    # for i in rows:
    #     print(i)
    l10=[]
    l2=[]
    k=0
    t=0
    for i in rows:
        # print(i)
        if k==0:
            
            dict50={}
            temp=0
            dict50["company_name"]=i[0]
            temp=i[0]
            # print(temp)
            l3={"name":i[1],"price":i[2],"stock":i[3],"description":i[4]}
            l10.append(l3)
            dict50["products"]=l10
            l2.append(dict50)
            
            # rc=rc-1
            k=1
            t=t+1
        else:
            if temp==i[0]:
                l4={"name":i[1],"price":i[2],"stock":i[3],"description":i[4]}
                dict26=l2[t-1]
                dict27=dict26["products"]
                l2.pop(t-1)
                l10.append(l4)
                dict50["products"]=l10
                l2.append(dict50)
            else:
                l10=[]
                l3={"name":i[1],"price":i[2],"stock":i[3],"description":i[4]}
                l10.append(l3)
                k=0
    return l2
    
def search_product(search_dict):
    l=[]
    for key in search_dict.items():
        l.append(key)
    count=len(l)
    p=1
    # print(count)
    query1="SELECT * FROM product WHERE "
    valuedict={} 
    for key,value in search_dict.items():
        if p<count:
            str1 = "product."+key+"=:value"+str(p)+" AND " 
            query1 = query1+str1    
        else:
            str1 =  "product."+key+"=:value"+str(p)
            query1 = query1 + str1 
        valuedict["value"+str(p)]=value   
        p=p+1
            
    # print(valuedict)
    # print(query1)
    result = conn.execute(query1,valuedict)
    rows = result.fetchall()
    # print(rows)
    return rows