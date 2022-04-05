import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/LIBRARY')
from userfunction import *
from flask import Flask,request
from flask_jwt_extended import jwt_required
from flask import Blueprint


userapi = Blueprint('userapi',__name__,url_prefix='/user')
 
@userapi.route('/signup',methods=['POST'])
def for_create():
    data1=request.get_json()
    return create(data1)


@userapi.route('/getbyid/<id>',methods=['GET'])
@jwt_required()
def for_get_by_id(id):    
    return getbyid(id)

@userapi.route('/update/<id>',methods=['PUT'])
@jwt_required()
def for_update(id):
    data3=request.get_json()
    return up_date(id,data3)

@userapi.route('/login',methods=['POST'])
def for_login():
    data2=request.get_json()
    return login(data2)
   
@userapi.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def for_delete(id):
    return deletebyid(id)

@userapi.route('/token/new/<id>',methods=['GET'])
@jwt_required(refresh=True)
def new_token(id):
    return create_newaccess_tokens(id)


        

    

            