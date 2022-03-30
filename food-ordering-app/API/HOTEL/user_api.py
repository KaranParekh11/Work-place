from flask import Flask,request
from API.HOTEL.funcforuser import *
from flask_jwt_extended import jwt_required
from flask import Blueprint
from API.HOTEL.datamanage import view_data

user_api = Blueprint('user_api',__name__,url_prefix='/user')
 
@user_api.route('/signup',methods=['POST'])
def for_create():
    data1=request.get_json()
    return create(data1)

@user_api.route('/viewdata',methods=['GET'])
# @jwt_required()
def for_view_data():
    return view_data()

@user_api.route('/getbyid/<id>',methods=['GET'])
@jwt_required()
def for_get_by_id(id):    
    return getbyid(id)

@user_api.route('/update/<id>',methods=['PUT'])
@jwt_required()
def for_update(id):
    data3=request.get_json()
    return up_date(id,data3)

@user_api.route('/login',methods=['POST'])
def for_login():
    data2=request.get_json()
    return login(data2)
   
@user_api.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def for_delete(id):
    return deletebyid(id)

@user_api.route('/token/new/<id>',methods=['GET'])
@jwt_required(refresh=True)
def new_token(id):
    return create_newaccess_tokens(id)


        

    

            