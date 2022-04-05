import json,datetime
import re
import hashlib
import os 
import uuid
import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/MODELS')
from user import *
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/UTILS')
from test1 import create_database_tabels
from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

def hash_password(password):
    password=password.encode()
    salt=os.urandom(16)
    salt_hex=salt.hex()
    digest=hashlib.pbkdf2_hmac('sha256',password,salt,100000)#hash_password(digest)
    digest_hex=digest.hex()
    return salt_hex,digest_hex

def login(data2):
    email=data2["email"]
    password=data2["password"]
    z=get_email(email)
    if z==True:
        x=get_password(email,password)
        user_id=x[0]
        salt=x[1]
        digest=x[2]
        w=authenticate(password,salt,digest)
        if w==True:
            y=create_token(email) 
            y1=y["refresh_token"] 
            insert_token(email,y1)
            return jsonify ("login suceesful",{"your user id":user_id},y) , 200
        else:
            return "please !! enter correct password. !!" , 401
    else:
        return "Enter correct email" , 401

def checkemail(email):
    regex = re.compile(r'[A-Za-z]+([A-Za-z0-9]+[-_]*)*@[A-Za-z]+(\.[A-Z|a-z]{2,})+')
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def checkpassword(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$^!%*#?&])[A-Za-z\d@$!^#%*?&]{8,}$')
    if(re.fullmatch(regex,password)):
        return True
    else:
        return False

def create(data1):
    email=data1["email"]
    password=data1["password"]
    x=checkemail(email)
    y=checkpassword(password)
    if x==False and y==False:
        return "enter valid email and password!!", 400
    elif x==False and y==True:
        return "enter valid email!", 400
    elif x==True and y==False:
        return "enter valid password!!", 400
    else:
        abc=hash_password(password)
        salt=abc[0]
        digest=abc[1]
        id=uuid.uuid4().hex
        dict1={"user_id":id,"salt":salt,"digest":digest}
        del data1["password"]
        data1.update(dict1) 
        insert_user_info(data1)
        return jsonify ("profile created success fully") , 201

def authenticate(newpass,salt,digest):
    salt1=bytes.fromhex(salt)
    newpass1=newpass.encode()
    newdigest=hashlib.pbkdf2_hmac('sha256',newpass1,salt1,100000)
    newdigest=newdigest.hex()
    if newdigest==digest:
        return True
    else:
        return False

def deletebyid(id=0):
    z1=delete_user_info(id)
    # print(z1)
    # view_data()
    if z1=="success":
        return "deleted succesfully!!!" , 200
    else:
        return "enter valid user id!!!" , 400

def up_date(id,data2):
    l=[]
    for i in data2.keys():
        i=i.capitalize()
        l.append(i)
    # print(l)
    if "Salt" in l or "Digest" in l or "Refresh_token" in l:
        return "unauthorized request from user", 400
    else:
        for (key,value) in data2.items():
            x = update_user_table(key,value,id)
        if x == "success":
            return "data updated successfully", 200
        else:
            return "enter correct user id for update!!!" , 400
    # view_data()
   
def getbyid(id):
    abc = get_data_by_id(id)
    if abc!="error":
        dict={"users":[
            {"User_id":abc[0],
            "Name":abc[1],
            "Gmail":abc[2],
            "D-O-B":abc[3],
            "Refresh_Token":abc[6]
            }
        ]}
        return jsonify(dict) , 200
    else:
        return "enter valid user id!!!" , 401

def create_token(email):
    expiers=datetime.timedelta(minutes=15)
    refresh_token=create_refresh_token(identity=email)
    access_token=create_access_token(identity=email,expires_delta=expiers)
    kar={"refresh_token":refresh_token,"access_token":access_token}
    return kar

def create_newaccess_tokens(id):
    hg=aces_token(id)
    if hg!=None:
        identity1=hg[0]
    else:
        return "enter valid user id" , 401
    expiers=datetime.timedelta(minutes=15)
    new_access_token=create_access_token(identity=identity1, expires_delta=expiers)
    new_refresh_token=create_refresh_token(identity=identity1)
    fl=update_user_table("Refresh_Token",new_refresh_token,id)
    # print(fl)
    if fl=="success":
        return jsonify({"new_access_token": new_access_token,"new_refresh_token":new_refresh_token}),200
    else:
        return "enter correct user id or refresh token!!!" , 401
    
    