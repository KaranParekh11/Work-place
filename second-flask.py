from flask import Flask,request
from funcfor2 import *
from flask_jwt_extended import jwt_required

app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super-secret"

@app.route('/signup',methods=['POST'])
def for_create():
    data1=request.get_json()
    return create(data1)

@app.route('/getbyid/<id>',methods=['GET'])
@jwt_required()
def for_get_by_id(id):    
    return getbyid(id)

@app.route('/update/<id>',methods=['PUT'])
@jwt_required()
def for_update(id):
    data3=request.get_json()
    return up_date(id,data3)

@app.route('/login',methods=['POST'])
def for_login():
    data2=request.get_json()
    return login(data2)
   
@app.route('/delete/<id>',methods=['DELETE'])
@jwt_required()
def for_delete(id):
    return deletebyid(id)

@app.route('/token/new',methods=['GET'])
@jwt_required(refresh=True)
def new_token():
    return create_newaccess_tokens()

if __name__== "__main__":
    data={"users":[]}
    with open('userdata.json',"w+") as f:
        json.dump(data,f,indent=4)
    app.run(debug=True)
        

    

            