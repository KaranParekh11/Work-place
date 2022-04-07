from API.userapi import User,Users
from API.companyapi import Company,Search,Pagination,Getall
from API.productapi import Product,Searchproduct,Productpagination,Getallproduct

def intialize_apiroutes(api):
    """ user api  """
    api.add_resource(Users,'/user/signup',endpoint='/user/signup',methods=['POST'])
    api.add_resource(User,'/user/login',endpoint='/user/login',methods=['POST'])
    api.add_resource(User,'/user/get/<id>',endpoint='/user/get/<id>',methods=['GET'])
    api.add_resource(User,'/user/update/<id>',endpoint='/user/update/<id>',methods=['PUT'])
    api.add_resource(User,'/user/delete/<id>',endpoint='/user/delete/<id>',methods=['DELETE'])
    api.add_resource(Users,'/user/newtoken/<id>',endpoint='/user/newtoken/<id>',methods=['GET'])

    """ company api """
    api.add_resource(Company,'/company/signup',endpoint='/company/signup',methods=['POST'])
    api.add_resource(Company,'/company/delete/<id>',endpoint='/company/delete/<id>',methods=['DELETE'])
    api.add_resource(Company,'/company/get/<id>',endpoint='/company/get/<id>',methods=['GET'])
    api.add_resource(Company,'/company/update/<id>',endpoint='/company/update/<id>',methods=['PUT'])
    api.add_resource(Search,'/company/search',endpoint='/company/search',methods=['GET'])
    api.add_resource(Getall,'/company/getall',endpoint='/company/getall',methods=['GET'])
    api.add_resource(Pagination,'/company/pagination',endpoint='/company/pagination',methods=['GET'])

    """ product api """
    api.add_resource(Product,'/product/signup/<id>',endpoint='/product/signup/<id>',methods=['POST'])
    api.add_resource(Product,'/product/get/<id>',endpoint='/product/get/<id>',methods=['GET'])
    api.add_resource(Product,'/product/update/<id>',endpoint='/product/update/<id>',methods=['PUT'])
    api.add_resource(Product,'/product/delete/<id>',endpoint='/product/delete/<id>',methods=['DELETE'])
    api.add_resource(Getallproduct,'/product/getall',endpoint='/product/getall',methods=['GET'])
    api.add_resource(Productpagination,'/product/pagination',endpoint='/product/pagination',methods=['GET'])
    api.add_resource(Searchproduct,'/product/search',endpoint='/product/search',methods=['GET'])
