import json,datetime
import re
import hashlib
import os
import uuid 
import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/MODELS')
from dishes import *
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/UTILS')
from test1 import create_database_tabels
from flask import jsonify

def create_dish_info(id,data):
    try:
        dd=data["Dishes"]
    except:
        dd=data["dishes"]
    dish_list=[]
    for (key,value) in dd.items():
        key=key.capitalize()
        dish_dict={}
        dish_dict["Dish_id"]=uuid.uuid4().hex
        dish_dict["Dish_name"]=key
        dish_dict["Price"]=value
        dish_dict["Hotel_id"]=id
        dish_list.append(dish_dict)
    x=insert_Dish_info(dish_list)
    return jsonify ("Dishes Menu created success fully",{"Dish_id":x}),200



def deletebyid(id=0):
    z2=delete_dish_info(id)
    if z2=="success":
        return "Dish deleted succesfully!!!"
    else:
        return "enter valid Dish id!!!"

def up_date(id,data2):
    ndictd={}
    for (key,value) in data2.items():
        key=key.capitalize()
        ndictd[key]=value
    for (key,value) in ndictd.items():
        ndish_dict={}
        key=key.capitalize()
        ndish_dict["Dish_name"]=key
        ndish_dict["Price"]=value
        ndish_dict["Dish_Id"]=id
    ab=update_Dish_info(ndish_dict)
    print(ab)
    if ab=="success":
        return "Dish data updated successfully" , 200
    else:
        return "unsuccessful operation for updating dish data!!!"
    

def datasearch(args):
    Dishes1=args.get('Dishes')
    if Dishes1!=None:
        Dishes=str(Dishes1)
        Dishes2=Dishes1.split(',')
        Dishes=[]
        for i in Dishes2:
            i=i.capitalize()
            Dishes.append(i)
    else:
        Dishes=[]
    ans=get_all_dish_info()
    data=ans["Hotels"]
    c=0
    x=[]
    y={}
    for i in range(len(data)):
        count=0
        z=data[i]
        if  Dishes!=[]:
            for a in Dishes:
                if a in z["Dishes"]:
                    count=count+1
            if count==len(Dishes):
                y=data[i]
                x.append(y)
        else:
            x=data
    if  x==[]:
        return "Dish data not found for this search"

    return jsonify(x)
    
def getall():
    z=get_all_hotel_info()
    return jsonify(z)
    
def getall_pagination(args):
    offset=args.get("offset")
    limit=args.get("limit")
    if offset!=None and limit!=None and limit!="0":
        offset=int(offset)
        limit=int(limit)
        zx=get_all_dish_info()
        cx=zx["Hotels"]
        # print(cx)
        count=len(cx)
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
            A=200
            B="Data retrieved by user." 
            D = True 
            ab=[]
            page_no=offset+1
            data_limit_end = page_no*limit
            data_limit_start=data_limit_end - limit
            for a in range(data_limit_start,data_limit_end):
                if a==count:
                    break
                ab.append(cx[a])
               
            C= {"Hotels":ab}
            # print(C)


        xyz = {
                "Statuscode":A,
                "message":B,
                "data":C,
                "success":D,
                "count":count,
                "Total page":total_page
              }
        return jsonify(xyz)
    else:
        return "Enter valid offset and limit value!!!"


    
    
    




