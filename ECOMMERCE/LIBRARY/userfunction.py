import json,datetime
import re
import hashlib
import os 
import uuid
import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/MODELS')
from user import *
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
from test1 import create_database_tabels
from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager

def date_validation(dob):
    if len(dob)==8:
        day=dob[0:2]
        month=dob[2:4]
        year=dob[4:]
    elif len(dob)==10:
        if '-' in dob:
            dob=dob.split('-') 
        elif '/' in dob:
            dob=dob.split('/')
        else:
            return "ENTER VALID DATE OR FORMAT"
        print(dob)
        day=dob[0]
        month=dob[1]
        year=dob[2]
    else:
        return "Enter in valid Format. e.g. ddmmyyyy OR dd-mm-yyyy OR dd/mm/yyyy"
    isValidDate = True
    try :
        datetime.datetime(int(year),
                          int(month), int(day))  
        if int(year)<1922:
            return "ENTER CORRECT BIRTH YEAR !!! TOO OLD."
        elif int(year)>1922 and int(year)<2004:
            None
        else:
            return "TOO YOUNG!! ENTER VALID D-O-B"
    except ValueError :
        isValidDate = False
    if(isValidDate) :
        return True
    else :
        return "Enter valid Date of Birth"


def hash_password(password):
    password=password.encode()
    salt=os.urandom(16)
    salt_hex=salt.hex()
    digest=hashlib.pbkdf2_hmac('sha256',password,salt,100000)#hash_password(digest)
    digest_hex=digest.hex()
    return salt_hex,digest_hex
def setmobileno(mobile):
    v=mobile[:-11:-1]
    nv=v[::-1]
    nv=int(nv)
    return nv

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
            return ["login succesful",{"your user id":user_id},y], 200
        else:
            return "please !! enter correct password !!", 401
    else:
        return "Enter correct email", 401

def checkmobile(mobileno):
    # mobileno=str(mobileno)
    regex=re.compile(r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6789]\d{9}$')
    if(re.fullmatch(regex, mobileno)):
        return True
    else:
        return False

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
    mobile=data1["mobileno"]
    dob=data1["dob"]
    w=date_validation(dob)
    z=checkmobile(mobile)
    x=checkemail(email)
    y=checkpassword(password)
    if x==False and y==False:
        return "enter valid email and password!!", 400
    elif x==False and y==True:
        return "enter valid email!", 400
    elif x==True and y==False:
        return "enter valid password!!", 400
    elif z==False:
        return "enter valid mobile no",400
    elif w!=True:
        return w,400
    else:
        abc=hash_password(password)
        mobileno=setmobileno(mobile)
        # print(abc)
        salt=abc[0]
        digest=abc[1]
        id=uuid.uuid4().hex
        dict1={"id":id,"salt":salt,"digest":digest,"mobileno":mobileno}
        del data1["password"]
        data1.update(dict1) 
        insert_user_info(data1)
        return "profile created success fully", 201

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
    
    for (key,value) in data2.items():
        key=key.lower()
        
        if key=="password":
            y=checkpassword(value)
            if y==False:
                return "Enter valid Password for update",400
            else:
                np=hash_password(value)
                salt=np[0]
                digest=np[1]
                # print(salt,digest)
                x=update_user_table("salt",salt,id)
                x=update_user_table("digest",digest,id)
        elif key=="email":
            z=checkemail(value)
            if z==False:
                return "Enter valid email for update",400
            else:
                x = update_user_table(key,value,id)
        elif key=="mobileno":
            z=checkmobile(value)
            if z==False:
                return "Enter valid email for update",400
            else:
                value=setmobileno(value)
                x = update_user_table(key,value,id)
        elif key=="dob":
            z=date_validation(value)
            if z!=True:
                return z,400
            else:
                x = update_user_table(key,value,id)
        else:
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
            {"Userid":abc[0],
            "Name":abc[1],
            "Email":abc[2],
            "Mobile No":abc[3],
            "D-O-B":abc[4],
            "Refresh_Token":abc[7]
            }
        ]}
        return dict , 200
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
    fl=update_user_table("refresh_Token",new_refresh_token,id)
    # print(fl)
    if fl=="success":
        return {"new_access_token": new_access_token,"new_refresh_token":new_refresh_token},200
    else:
        return "enter correct user id or refresh token!!!" , 401
    
def checkput1(data1):
    list1=[]
    v=0
    for i in data1.keys():
        list1.append(i)
    l2=['name','password','email','mobileno','dob']
    for i in list1:
        if i in l2:
            v="success"
            continue
        else:
            v=0
            break
    return v