import json
from random import randint
import re
import hashlib
import os 
import uuid
import sys
sys.path.insert(0,'E:/KARAN PY/flask-mail/MODELS')
from user import *
from flask import jsonify
from flask_mail import  Message


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
        # print(dob)
        day=dob[0]
        month=dob[1]
        year=dob[2]
    else:
        return "Enter in valid Format. e.g. ddmmyyyy OR dd-mm-yyyy OR dd/mm/yyyy"
    isValidDate = True
    try :
        dt.datetime(int(year),
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
    # print(data2)
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
            return ["login succesful",{"your user id":user_id}], 200
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

def accountverify(email):
    x=get_email(email)
    if x==True:
        ab=isverify1(email)
        abc=otpgenerate()
        msg = Message('OTP FOR VERFICATION', sender = 'loganxmen1110@gmail.com', recipients = [email])
        msg.body = str(abc)
        # mail.send(msg)
        if ab =='success':
            insertotp(email,abc)
            return True,"OTP SENT",msg,abc, 200
        elif ab=='verified':
            return "ACCOUNT ALREADY VERIFIED",200
        else:
            return "ERROR" , 400
    else:
        return "ENTER VALID EMAIL ID",400


def otpgenerate():
    otp=randint(100000,999999)
    return otp


def verification(email,otp):
    z=dt.datetime.now()
    v=verified(email,otp,z)
    if v=="success":
        return "YOUR ACCOUNT VERIFIED SUCCESSFULLY",200
    elif v=="failure":
        return "OTP EXPIRED",400
    else:
        return "Enter valid otp or Email id",400


def fp(email):
    x=get_email(email)
    if x==True:
        ab=isaccverified(email)
        OTP=otpgenerate()
        msg = Message('OTP FOR FOGOT PASSWORD', sender = 'loganxmen1110@gmail.com', recipients = [email])
        msg.body = str(OTP)
        # mail.send(msg)
        if ab =='verified':
            insertotp(email,OTP)
            return True,"OTP SENT",msg,OTP,200
        else:
            return "ACCOUNT NOT VERIFIED" , 400,
    else:
        return "ENTER VALID EMAIL ID",400


def rp(data):
    email=data['email']
    np=data['newpassword']
    otp=data['otp']
    z=dt.datetime.now()
    abc=checkpassword(np)
    if abc!=True:
        return "Enter valid password. min (8 digit,1 capital,1 small and 1 special character) necessary.",400
    else:
        pw=hash_password(np)
        salt=pw[0]
        digest=pw[1]
        # print(salt,digest)
        v=forreset(email,otp,np,z,salt,digest)
        if v=="success":
            return "YOUR PASSWORD RESET SUCCESSFULLY",200
        elif v=="failure":
            return "OTP EXPIRED",400
        else:
            return "Enter valid otp or Email id",400