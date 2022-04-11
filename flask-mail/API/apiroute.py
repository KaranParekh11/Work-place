from API.userapi import User,Users,Forotp,Verifyemail,Forgotpassword,Resetpassword


def intialize_apiroutes(api):
    """ user api  """
    api.add_resource(Users,'/user/signup',endpoint='/user/signup',methods=['POST'])
    api.add_resource(User,'/user/login',endpoint='/user/login',methods=['POST'])
    api.add_resource(Verifyemail,'/user/verify',endpoint='/user/verify',methods=['POST'])
    api.add_resource(Forotp,'/user/otp',endpoint='/user/otp',methods=['POST'])
    api.add_resource(Forgotpassword,'/user/forgotpassword',endpoint='/user/forgotpassword',methods=['POST'])
    api.add_resource(Resetpassword,'/user/resetpassword',endpoint='/user/resetpassword',methods=['POST'])


    


    

   
