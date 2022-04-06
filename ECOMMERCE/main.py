from flask import Flask
from flask_restful import Resource,Api
# from API.companyapi import *
# from API.productapi import *
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow
import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
from test1 import create_database_tabels
# from API.apiroute import user_list
from API.userapi import User,Users
from API.companyapi import Company,Search,Pagination,Getall
from API.productapi import Product,Searchproduct,Productpagination,Getallproduct


app = Flask(__name__)
api = Api(app)
# ma = Marshmallow(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
    

api.add_resource(Users,'/user/signup',endpoint='/user/signup',methods=['POST'])
api.add_resource(User,'/user/login',endpoint='/user/login',methods=['POST'])
api.add_resource(User,'/user/get/<id>',endpoint='/user/get/<id>',methods=['GET'])
api.add_resource(User,'/user/update/<id>',endpoint='/user/update/<id>',methods=['PUT'])
api.add_resource(User,'/user/delete/<id>',endpoint='/user/delete/<id>',methods=['DELETE'])
api.add_resource(Users,'/user/newtoken/<id>',endpoint='/user/newtoken/<id>',methods=['GET'])

api.add_resource(Company,'/company/signup',endpoint='/company/signup',methods=['POST'])
api.add_resource(Company,'/company/delete/<id>',endpoint='/company/delete/<id>',methods=['DELETE'])
api.add_resource(Company,'/company/get/<id>',endpoint='/company/get/<id>',methods=['GET'])
api.add_resource(Company,'/company/update/<id>',endpoint='/company/update/<id>',methods=['PUT'])
api.add_resource(Search,'/company/search',endpoint='/company/search',methods=['GET'])
api.add_resource(Getall,'/company/getall',endpoint='/company/getall',methods=['GET'])
api.add_resource(Pagination,'/company/pagination',endpoint='/company/pagination',methods=['GET'])

api.add_resource(Product,'/product/signup/<id>',endpoint='/product/signup/<id>',methods=['POST'])
api.add_resource(Product,'/product/get/<id>',endpoint='/product/get/<id>',methods=['GET'])
api.add_resource(Product,'/product/update/<id>',endpoint='/product/update/<id>',methods=['PUT'])
api.add_resource(Product,'/product/delete/<id>',endpoint='/product/delete/<id>',methods=['DELETE'])
api.add_resource(Getallproduct,'/product/getall',endpoint='/product/getall',methods=['GET'])
api.add_resource(Productpagination,'/product/pagination',endpoint='/product/pagination',methods=['GET'])
api.add_resource(Searchproduct,'/product/search',endpoint='/product/search',methods=['GET'])










if __name__=="__main__":
    app.run(debug=True)
