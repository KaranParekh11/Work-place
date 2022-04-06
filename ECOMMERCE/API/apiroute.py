

user_list=["api.add_resource(Users,'/user/signup',endpoint='/signup',methods=['POST'])",
"api.add_resource(User,'/user/login',endpoint='/login',methods=['POST'])",
"api.add_resource(User,'/user/get/<id>',endpoint='/get/<id>',methods=['GET'])",
"api.add_resource(User,'/user/update/<id>',endpoint='/update/<id>',methods=['PUT'])",
"api.add_resource(User,'/user/delete/<id>',endpoint='/delete/<id>',methods=['DELETE'])",
"api.add_resource(Users,'/user/newtoken/<id>',endpoint='/newtoken/<id>',methods=['GET'])"]