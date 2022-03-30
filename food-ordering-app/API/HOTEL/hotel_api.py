from flask import Flask,request
from API.HOTEL.funcforhotel import *
from flask_jwt_extended import jwt_required
from flask import Blueprint



hotel_api = Blueprint('hotel_api',__name__,url_prefix="/hotel")
 
@hotel_api.route('/getall',methods=['GET'])
# @jwt_required()
def for_get_all():
    return getall()

@hotel_api.route('/signup',methods=['POST'])
@jwt_required()
def for_create():
    data1=request.get_json()
    return create(data1)

@hotel_api.route('/update/<id>',methods=['PUT'])
# @jwt_required()
def for_update(id):
    data3=request.get_json()
    return up_date(id,data3)
   
@hotel_api.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def for_delete(id):
    return deletebyid(id)

@hotel_api.route('/datasearch',methods=['GET'])
@jwt_required()
def data_search():
    args=request.args
    return datasearch(args)

@hotel_api.route('/get-all',methods=['GET'])
# @jwt_required()
def for_get_data():
    args=request.args
    return getall_pagination(args)

        

    

            