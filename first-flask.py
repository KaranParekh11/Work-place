from flask import Flask,request
from functions import *

app = Flask(__name__)

@app.route('/create',methods=['POST'])
def for_create():
    data1=request.get_json()
    return create(data1)

@app.route('/update/<id>',methods=['PUT'])
def for_update(id):
    data2=request.get_json()
    return up_date(id,data2)

@app.route('/getbyid/<id>',methods=['GET'])
def for_get_by_id(id):    
    return getbyid(id)
   
@app.route('/getall',methods=['GET'])
def for_get_all():
    return getall()

@app.route('/delete/<id>',methods=['DELETE'])
def for_delete(id):
    return deletebyid(id)




if __name__== "__main__":
    data={"users":[]}
    with open('db1.json',"w+") as f:
        json.dump(data,f,indent=4)
    app.run(debug=True)
        

    

            