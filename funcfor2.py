import json,datetime
import re
import hashlib
import os 

from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_jwt_extended import get_jwt_identity
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
    with open('userdata.json',"r") as f:
        rawdata = json.load(f)
        data=rawdata["users"]
        count=0
        c=0
        for i in data:
            if i["email"]==email:
                x=data[count]
                salt=x["salt"]
                digest=x["digest"]
                w=authenticate(password,salt,digest)
                if w==True:
                    y=create_token(email)
                    y1=y["refresh_token"]
                    x["refresh_token"]=y1   
                    with open('userdata.json',"w") as f:
                        json.dump(rawdata,f,indent=4) 
                    return jsonify ("login suceesful",y),200
                else:
                    x = "please !! enter correct password. !!"
                c=1
                break
            else:
                count=count+1
                continue
        if count==len(data) and c==0:
            x="please !! Enter correct email id. !!"
    return x
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
        return "enter valid email!",400
    elif x==True and y==False:
        return "enter valid password!!",400
    else:
        abc=hash_password(password)
        salt=abc[0]
        digest=abc[1]
        dict1={"salt":salt,"digest":digest}
        del data1["password"]
        data1.update(dict1)
        with open('userdata.json',"r") as f:
            rawdata = json.load(f)
            rawdata["users"].append(data1)
        with open('userdata.json',"w") as f:
            json.dump(rawdata,f,indent=4)   
        return jsonify ("profile created success fully") , 200

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
    with open('userdata.json',"r+") as f:
        id=int(id)
        rawdata = json.load(f)
        data=rawdata["users"]
        count=0
        c=0
        for i in data:
            if i["id"]==id:
                data.pop(count)
                x="data deleted successfully"
                c=1
                break
            else:
                count=count+1
                continue
        if count==len(data) and c==0:
            x="data not found for this id or already deleted."
        with open('userdata.json',"w") as f:
            json.dump(rawdata,f,indent=4)
    return x

def up_date(id,data2):
    for i in data2.keys():
        if i=="salt" or i=="digest" or i=="refresh_token":
            return "unauthorized request from user",400
        else:
            with open('userdata.json',"r+") as f:
                id=int(id)
                rawdata = json.load(f)
                data=rawdata["users"]
                count=0
                c=0
                for i in data:
                    if i["id"]==id:
                        x=data[count]
                        x.update(data2)
                        z={}
                        for (key,value) in x.items():
                            if key!="salt" and key!="refresh_token" and key!="digest":
                                z[key]=value
                        return jsonify ("updated successfully",z),200
                        break
                    else:
                        count=count+1
                        continue
                if count==len(data) and c==0:
                    x="data can not be update for this id"
                with open('userdata.json',"w") as f:
                    json.dump(rawdata,f,indent=4)
    return x

def getbyid(id=0):
    with open('userdata.json',"r") as f:
        id=int(id)
        rawdata = json.load(f)
        data=rawdata["users"]
        count=0
        c=0
        for i in data:
            if i["id"]==id:
                dict1=data[count]
                x={}
                for (key,value) in dict1.items():
                    if key!="salt" and key!="digest" and key!="refresh_token":
                        x[key]=value
                c=1
                break
            else:
                count=count+1
                continue
        if count==len(data) and c==0:
            x="data not found for this id"
    return jsonify ( "your data" , x) , 200

def create_token(email):
    expiers=datetime.timedelta(seconds=30)
    refresh_token=create_refresh_token(identity=email)
    access_token=create_access_token(identity=email,expires_delta=expiers)
    kar={"refresh_token":refresh_token,"access_token":access_token}
    return kar

def create_newaccess_tokens():
    identity1=get_jwt_identity()
    expiers=datetime.timedelta(seconds=30)
    new_access_token=create_access_token(identity=identity1, expires_delta=expiers)
    new_refresh_token=create_refresh_token(identity=identity1)
    with open('userdata.json',"r") as f:
            rawdata = json.load(f)
            data1=rawdata['users']
            for i in data1:
                if i["email"]==identity1:
                    i["refresh_token"]=new_refresh_token
                else:
                    continue
    with open('userdata.json',"w") as f:
            json.dump(rawdata,f,indent=4)  
    return jsonify({"new_access_token": new_access_token,"new_refresh_token":new_refresh_token}),200


