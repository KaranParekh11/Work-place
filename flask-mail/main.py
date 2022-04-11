from flask import Flask,make_response,jsonify,request
from flask_restful import Resource,Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail, Message



import sys
sys.path.insert(0,'E:/KARAN PY/flask-mail/UTILS')
from dbcreate import create_database_tabels
from API.apiroute import intialize_apiroutes
from jsonschema import ValidationError
from mailfile import mail,callmail


app = Flask(__name__)
api = Api(app)
callmail(app)
mail.init_app(app)

# @app.route('/user',methods=['POST'])
# def for_update():
#     data2=request.get_json()
#     email=data2['email']
#     # print(email)
#     msg=Message('Hello', sender = 'loganxmen1110@gmail.com', recipients = [email])
#     msg.body = "Hello Flask message sent from Flask-Mail"
#     mail.send(msg)
#     return "success"
    
intialize_apiroutes(api)
@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'error': original_error.message}), 400)

if __name__=="__main__":
    app.run(debug=True)
