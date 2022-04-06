import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/LIBRARY')
from userfunction import *
from flask import Flask,request,jsonify,make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource



class Users(Resource):
    def post(self):
        data1=request.get_json()
        x=create(data1)
        return make_response(jsonify(x[0]),x[1])

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
    def put(self,id):
        data3=request.get_json()
        x=up_date(id,data3)
        return make_response(jsonify(x[0]),x[1])

    def post(self):
        data2=request.get_json()
        x=login(data2)
        return make_response(jsonify(x[0][0:3]),x[1])
        
    
    @jwt_required()
    def delete(self,id):
        x=deletebyid(id)
        return make_response(jsonify(x[0]),x[1])
       
    

    


 






    



        

    

            