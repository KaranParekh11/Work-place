import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/LIBRARY')
from productfunction import *
from flask import Flask,request,jsonify,make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask_restful import reqparse
from flask_expects_json import expects_json
from API.schema import schema6,schema7
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
import log
import logging

log = logging.getLogger(__name__)


class Product(Resource):
    @expects_json(schema6)
    def post(self,id):
        data1=request.get_json()
        z=checkproduct(data1)
        list1=[]
        for i in data1.keys():
            list1.append(i)
        if len(list1)==1:
            if z=="success":
                x=create_product_info(id,data1)
                return make_response(jsonify(x[0]),x[1])
            else:
                log.warning("invalid product specification")
                return make_response(jsonify("invalid product specification"),400)
        else:
            log.warning('ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!for product sign up')
            return make_response(jsonify("ENTER VALID DATA. NO EXTRA DATA ACCEPTED!!!",{"BAD REQUEST":400}),400)


    @jwt_required()
    def delete(self,id):
        x=deletebyid(id)
        return make_response(jsonify(x[0]),x[1])

    @jwt_required()
    def get(self,id):
        x=getbyid(id)
        return make_response(jsonify(x[0]),x[1])

    @jwt_required()
    @expects_json(schema7)
    def put(self,id):
        data3=request.get_json()
        x=up_date(id,data3)
        return make_response(jsonify(x[0]),x[1])

class Searchproduct(Resource):
    @jwt_required()
    def get(self):
        parser = reqparse.RequestParser()
        l=["name",'price','stock','description']
        for i in l:
            parser.add_argument(i)
        args = parser.parse_args()
        x=datasearch(args)
        return make_response(jsonify(x[0]),x[1])

class Getallproduct(Resource):
    @jwt_required()
    def get(self):
        x=getall()
        # return jsonify("hello")
        return make_response(jsonify(x[0]),x[1])

class Productpagination(Resource):
    @jwt_required()
    def get(self):
        args=request.args
        x=getall_pagination(args)
        # return jsonify("hello")
        return make_response(jsonify(x[0]),x[1])


        

    
       
    

    




    

            