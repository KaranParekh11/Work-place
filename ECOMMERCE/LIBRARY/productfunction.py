import json,datetime
import re
import hashlib
import os
import uuid 
import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/MODELS')
from product import *
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
import log
import logging
from test1 import create_database_tabels
from flask import jsonify

log = logging.getLogger(__name__)

def create_product_info(id,data):
    product_list=[]
    for i in data["products"]:
        product_dict={}
        product_dict["id"]=uuid.uuid4().hex
        x=product_dict["id"]
        for (key,value) in i.items():
            key=key.lower()
            product_dict[key]=value
        product_list.append(product_dict)
    cv=insert_product_info(id,product_list)
    if cv=="success":
        log.info("Product inserted successfully for company id:"+id)
        return ["Product inserted success fully",{"product_id":x}],200
    else:
        log.warning("Product not inserted successfully.kindly check company id(invalid company id):"+id)
        return "Product not inserted.kindely check company id",400



def deletebyid(id=0):
    z2=delete_product_info(id)
    if z2=="success":
        log.info("Product data deleted successfully for product id:"+id)
        return "product data deleted succesfully!!!",200
    else:
        log.warning("Product not deleted successfully.kindly check product id(invalid product id):"+id)
        return "enter valid product id!!!",400

def up_date(id,data2):
    ab=update_product_info(id,data2)
    # print(ab)
    if ab == "success":
        log.info("Product data updated successfully for product id:"+id)
        return "product data updated successfully" , 200
    else:
        log.warning("Product not updated successfully.product id:"+id)
        return "unsuccessful operation for updating product data!!!",400
    

def datasearch(args):
    search_dict={}
    for key,value in args.items():
        if value!=None:
            search_dict[key]=value
        else:
            continue
    # print(search_dict)
    if search_dict == {}:
        bn=get_all_product_info()
        return bn,200
    else:
        abcd=search_product(search_dict)
        if abcd == []:
            log.warning("enter valid value of parameter for search.")
            return "enter valid value of parameter", 200
        else:
        # print(abcd)
            dict10=[]
            for abc in abcd:
                dict1 ={"id":abc[0],
                    "name":abc[1],
                    "price":abc[2],
                    "stock":abc[3],
                    "discription":abc[4],
                    }
                dict10.append(dict1)
            # print(dict10)
        log.info('product search successfully.')
        return dict10,200

def getall():
    z=get_all_product_info()
    return z,200
    
def getall_pagination(args):
    offset=args.get("offset")
    limit=args.get("limit")
    if offset!=None and limit!=None and limit!="0":
        offset=int(offset)
        limit=int(limit)
        cx=get_all_product_info()
        b=[]
        for i in cx:
            for x in i["products"]:
                b.append(x)
        # print(cx)
        count=len(b)
        if count%limit==0:
            total_page = count/limit
        else:
            total_page = int(count/limit) + 1

        if offset+1 > total_page:
            A=400
            B="Data not retrieved by user."
            C = "error"
            D = False 
        else:
            # ac=[]
            A=200
            B="Data retrieved by user." 
            D = True 
            ac=[]
            page_no=offset+1
            data_limit_end = page_no*limit
            data_limit_start=data_limit_end - limit
            for a in range(data_limit_start,data_limit_end):
                if a==count:
                    break
                ac.append(b[a])
            
            C= {"products":ac}
            # print(C)


        xyz = {
                "Statuscode":A,
                "message":B,
                "data":C,
                "success":D,
                "count":count,
                "Total page":total_page
              }
        log.info("pagination done for offset:"+str(offset)+"limit"+str(limit))
        return xyz,200
    else:
        log.warning("Enter valid offset and limit value!!!for pagination")
        return "Enter valid offset and limit value!!!",400

def checkproduct(data1):
    listproduct=data1['products']
    count=len(listproduct)
    l2=[]
    for i in listproduct:
        for y in i.keys():
            l2.append(y)
    actuallist=['name','price','stock','description']
    v=0
    for i in l2:
        if i in actuallist and len(l2)==(4*count):
            v="success"
        else:
            v=0
            break
    return v
    

    
    
    




