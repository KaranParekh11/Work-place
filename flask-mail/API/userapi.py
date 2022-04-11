import sys
sys.path.insert(0,'E:/KARAN PY/flask-mail/LIBRARY')
sys.path.insert(0,'E:/KARAN PY/flask-mail/UTILS')
from userfunction import *
from mailfile import mail
from flask import Flask,request,jsonify,make_response
from flask_restful import Resource
from flask_expects_json import expects_json
from API.schema import schema1,schema2,schema3,schema4,schema5
from flask_mail import Mail, Message




class Users(Resource):        
    @expects_json(schema1)
    def post(self):
        data1=request.get_json()
        # print(data1)
        list1=[]
        for i in data1.keys():
            list1.append(i)
        if len(list1)==5:
            x=create(data1)
            return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)

class User(Resource):        

    @expects_json(schema2)
    def post(self):
        data2=request.get_json()
        list2=[]
        for i in data2.keys():
            list2.append(i)
        if len(list2)==2:
            x=login(data2)
            return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)

class Forotp(Resource):
    @expects_json(schema3)
    def post(self):
        data=request.get_json()
        email=data['email']
        list2=[]
        for i in data.keys():
            list2.append(i)
        if len(list2)==1:
            x=accountverify(email)
            if x[0]==True:
                msg=x[2]
                # print(msg)
                mail.send(msg)
                return make_response(jsonify(x[1],{"OTP":x[3]}),x[4])
            else:
                return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER ONLY EMAIL. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)

class Verifyemail(Resource):
    @expects_json(schema4)

    def post(self):
        data=request.get_json()
        list2=[]
        for i in data.keys():
            list2.append(i)
        if len(list2)==2:
            otp=data['otp']
            email=data['email']
            x=verification(email,otp)
            return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER ONLY EMAIL. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)


class Forgotpassword(Resource):
    @expects_json(schema3)
    def post(self):
        data=request.get_json()
        email=data['email']
        list2=[]
        for i in data.keys():
            list2.append(i)
        if len(list2)==1:
            x=fp(email)
            if x[0]==True:
                msg=x[2]
                # print(msg)
                mail.send(msg)
                return make_response(jsonify(x[1],{"OTP":x[3]}),x[4])
            else:
                return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER ONLY EMAIL. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)



class Resetpassword(Resource):
    @expects_json(schema5)
    def post(self):
        data=request.get_json()
        list2=[]
        for i in data.keys():
            list2.append(i)
        if len(list2)==3:
            x=rp(data)
            return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER ONLY EMAIL. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)
            

     


    
        
        
    
    
       
    

    


 






    



        

    

            