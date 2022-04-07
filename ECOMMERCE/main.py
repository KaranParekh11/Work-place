from flask import Flask,make_response,jsonify
from flask_restful import Resource,Api
# from API.companyapi import *
# from API.productapi import *
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
# from flask_marshmallow import Marshmallow
import sys
sys.path.insert(0,'E:/KARAN PY/ECOMMERCE/UTILS')
from test1 import create_database_tabels
from API.apiroute import intialize_apiroutes
from jsonschema import ValidationError

app = Flask(__name__)
api = Api(app)
# ma = Marshmallow(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
    
intialize_apiroutes(api)
@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'error': original_error.message}), 400)

if __name__=="__main__":
    app.run(debug=True)
