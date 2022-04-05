from flask import Blueprint,Flask
from API.userapi import *
from API.hotelapi import *
from API.dishesapi import *
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import sys
sys.path.insert(0,'E:/KARAN PY/MANAGEMENT/UTILS')
from test1 import create_database_tabels

def create_app():
    app=Flask(__name__)
    jwt = JWTManager(app)
    app.config["JWT_SECRET_KEY"] = "super-secret"
    app.register_blueprint(userapi)
    app.register_blueprint(hotelapi)
    app.register_blueprint(dishesapi)
    return app

if __name__=="__main__":
    app=create_app()
    app.run(debug=True)
