from flask import Blueprint,Flask
from API.HOTEL.hotel_api import *
from API.HOTEL.user_api import *
from flask_jwt_extended import jwt_required

def create_app():
    app=Flask(__name__)
    jwt = JWTManager(app)
    app.config["JWT_SECRET_KEY"] = "super-secret"
    app.register_blueprint(hotel_api)
    app.register_blueprint(user_api)
    return app

if __name__=="__main__":
    app=create_app()
    app.run(debug=True)
