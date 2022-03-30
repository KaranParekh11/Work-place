import json,datetime
import re
import hashlib
import os
import uuid 

from API.HOTEL.datamanage import *
from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

def create(data1):
    create_database_tables()
    dicth={}
    dictd={}
    for (key,value) in data1.items():
        key=key.capitalize()
        if key!="Dishes":
            dicth[key]=value
        else:
            dictd[key]=value
    hotel_id=uuid.uuid4().hex
    dh={"Hotel_id":hotel_id}
    dicth.update(dh)
    dd=dictd["Dishes"]
    dish_list=[]
    for (key,value) in dd.items():
        key=key.capitalize()
        dish_dict={}
        dish_dict["Dish_id"]=uuid.uuid4().hex
        dish_dict["Dish_name"]=key
        dish_dict["Price"]=value
        dish_dict["Hotel_id"]=hotel_id
        dish_list.append(dish_dict)
    # for i in dish_list:
    #     print(i)
    # print(dish_list)
    # print(dicth)
    # print(dd)
    insert_hotel_info(dicth)
    insert_Dish_info(dish_list)
    return jsonify ("Hotel profile created success fully") , 200

def deletebyid(id=0):
    z1=delete_hotel_info(id)
    z2=delete_dish_info(id)
    if z1=="success" and z2=="success":
        return "deleted succesfully!!!"
    else:
        return "enter valid user id!!!"

def up_date(id,data2):
    ndicth={}
    ndictd={}
    # print(data2)
    for (key,value) in data2.items():
        key=key.capitalize()
        if key!="Dishes":
            if key=="Hotel_name":
                value=value.capitalize()
                ndicth[key]=value
            else:
                ndicth[key]=value
            print(ndicth)
        else:
            ndictd[key]=value
    dh={"Hotel_id":id}
    ndicth.update(dh)
    av=update_hotel_info(id,ndicth)
    # print(ndicth)
    if ndictd!={}:
        dd=ndictd["Dishes"]
        ndish_list=[]    
        for (key,value) in dd.items():
            ndish_dict={}
            key=key.capitalize()
            ndish_dict["Dish_name"]=key
            ndish_dict["Price"]=value
            ndish_dict["Hotel_id"]=id
            ndish_list.append(ndish_dict)
        update_Dish_info(id,ndish_list)
    
    
    return jsonify (av) , 200

def datasearch(args):
    star=args.get('Star')
    # print(type(star))
    Dishes1=args.get('Dishes')
    hotelname=args.get('Hotelname')
    if hotelname!=None:
        hotelname=str(hotelname)
        hotelname=hotelname.capitalize()
    # print(hotelname)
    if star!=None:
        star=int(star)
    # print(star,type(star))

    if Dishes1!=None:
        Dishes=str(Dishes1)
        Dishes2=Dishes1.split(',')
        Dishes=[]
        for i in Dishes2:
            i=i.capitalize()
            Dishes.append(i)
    else:
        Dishes=[]
    # print(Dishes)
    # L={"Hotelname":hotelname,"Star":star,"Dishes":Dishes}
    ans=get_all_hotel_info()
    data=ans["Hotels"]
    c=0
    x=[]
    y={}
    for i in range(len(data)):
        count=0
        z=data[i]
        # print(z)
        # print(type(z["Star"]),type(z["Hotel_name"]))
        if  hotelname!=None and star!=None and Dishes!=[]:
            for a in Dishes:
                if a in z["Dishes"]:
                    count=count+1
            if count==len(Dishes) and z['Hotel_name']==hotelname and z["Star"]==star:
                y=data[i]
                x.append(y)
        elif hotelname!=None and star==None and Dishes==[]:
            if z["Hotel_name"]==hotelname:
                y=data[i]
                x.append(y)
        elif hotelname==None and star!=None and Dishes==[]:
            if z["Star"]==star:
                y=data[i]
                # print(y)
                x.append(y)
                # print(x)
        elif hotelname==None and star==None and Dishes!=[]:
            for a in Dishes:
                if a in z["Dishes"]:
                    count=count+1
            if count==len(Dishes):
                y=data[i]
                x.append(y)
        elif hotelname!=None and star!=None and Dishes==[]:
            if z["Hotel_name"]==hotelname and z["Star"]==star:
                y=data[i]
                x.append(y)
        elif hotelname!=None and star==None and Dishes!=[]:
            for a in Dishes:
                if a in z["Dishes"]:
                    count=count+1
            if count==len(Dishes) and z['Hotel_name']==hotelname:
                y=data[i]
                x.append(y)
        elif hotelname==None and star!=None and Dishes!=[]:
            for a in Dishes:
                if a in z["Dishes"]:
                    count=count+1
            if count==len(Dishes) and z['Star']==star:
                y=data[i]
                x.append(y)
        else:
            x=data
    # print(x)
    if  x==[]:
        return "hotel data not found for this search"

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
        zx=get_all_hotel_info()
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
            print(C)


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


    
    
    




