import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/LIBRARY')
from companyfunction import *
from flask import Flask,request,jsonify,make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from flask_expects_json import expects_json
from API.schema import schema4,schema5

class Company(Resource):
    @expects_json(schema4)
    def post(self):
        data1=request.get_json()
        list1=[]
        for i in data1.keys():
            list1.append(i)
        if len(list1)==6:
            x=create_company_info(data1)
            return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)
        

    @jwt_required()
    def delete(self,id):
        x=deletebyid(id)
        return make_response(jsonify(x[0]),x[1])

    @jwt_required()
    def get(self,id):
        x=getbyid(id)
        return make_response(jsonify(x[0]),x[1])

    @expects_json(schema5)
    @jwt_required()
    def put(self,id):
        data3=request.get_json()
        v=checkput(data3)
        if v=="success":
            x=up_date(id,data3)
            return make_response(jsonify(x[0]),x[1])
        else:
            return make_response(jsonify("ENTER VALID DATA AND NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)

class Search(Resource):
    @jwt_required()
    def get(self):
        parser = reqparse.RequestParser()
        l=["name",'category','website','days','time','address']
        for i in l:
            parser.add_argument(i)
        args = parser.parse_args()
        x=datasearch(args)
        return make_response(jsonify(x[0]),x[1])
        
class Getall(Resource):
    @jwt_required()
    def get(self):
        x=getall()
        # return jsonify("hello")
        return make_response(jsonify(x[0]),x[1])

class Pagination(Resource):
    @jwt_required()
    def get(self):
        args=request.args
        x=getall_pagination(args)
        # return jsonify("hello")
        return make_response(jsonify(x[0]),x[1])
    
 