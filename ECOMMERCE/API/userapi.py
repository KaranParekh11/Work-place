import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/LIBRARY')
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
import log
import logging
from userfunction import *
from flask import Flask,request,jsonify,make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask_expects_json import expects_json
from API.schema import schema1,schema2,schema3

log = logging.getLogger(__name__)

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
            log.warning('ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!for user sign up')
            return make_response(jsonify("ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)


    @jwt_required(refresh=True)
    def get(self,id):
        x=create_newaccess_tokens(id)
        return make_response(jsonify(x[0]),x[1])

class User(Resource):
    @jwt_required()
    def get(self,id):
        x=getbyid(id)
        return make_response(jsonify(x[0]),x[1])
        

    @jwt_required()
    @expects_json(schema3)
    def put(self,id):
        data1=request.get_json()
        v=checkput1(data1)
        if v=="success":
            x=up_date(id,data1)
            return make_response(jsonify(x[0]),x[1])
        else:
            log.warning('ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!for data update.user id:'+id)
            return make_response(jsonify("ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)

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
            log.warning('ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!for login user')
            return make_response(jsonify("ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)
        
        
    
    @jwt_required()
    def delete(self,id):
        x=deletebyid(id)
        return make_response(jsonify(x[0]),x[1])
       
    

    


 






    



        

    

            