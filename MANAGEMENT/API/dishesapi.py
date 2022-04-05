import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/LIBRARY')
from dishfunction import *
from flask import Flask,request
from flask_jwt_extended import jwt_required
from flask import Blueprint



dishesapi = Blueprint('dishesapi',__name__,url_prefix="/dishes")
 
@dishesapi.route('/getall',methods=['GET'])
@jwt_required()
def for_get_all():
    return getall()

@dishesapi.route('/signup/<id>',methods=['POST'])
@jwt_required()
def for_create(id):
    data=request.get_json()
    return create_dish_info(id,data)

@dishesapi.route('/update/<id>',methods=['PUT'])
@jwt_required()
def for_update(id):
    data3=request.get_json()
    return up_date(id,data3)
   
@dishesapi.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def for_delete(id):
    return deletebyid(id)

@dishesapi.route('/datasearch',methods=['GET'])
@jwt_required()
def data_search():
    args=request.args
    return datasearch(args)

@dishesapi.route('/get-all',methods=['GET'])
@jwt_required()
def for_get_data():
    args=request.args
    return getall_pagination(args)
