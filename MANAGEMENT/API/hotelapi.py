import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/LIBRARY')
from hotelfunction import *
from flask import Flask,request
from flask_jwt_extended import jwt_required
from flask import Blueprint



hotelapi = Blueprint('hotelapi',__name__,url_prefix="/hotel")
 
@hotelapi.route('/getall',methods=['GET'])
@jwt_required()
def for_get_all():
    return getall()

@hotelapi.route('/signup',methods=['POST'])
@jwt_required()
def for_create():
    data1=request.get_json()
    return create_hotel_info(data1)

@hotelapi.route('/update/<id>',methods=['PUT'])
@jwt_required()
def for_update(id):
    data3=request.get_json()
    return up_date(id,data3)
   
@hotelapi.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def for_delete(id):
    return deletebyid(id)

@hotelapi.route('/datasearch',methods=['GET'])
@jwt_required()
def data_search():
    args=request.args
    return datasearch(args)

@hotelapi.route('/get-all',methods=['GET'])
@jwt_required()
def for_get_data():
    args=request.args
    return getall_pagination(args)

        

    

            