from flask_mail import Mail, Message
mail=Mail()
def callmail(app):
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'loganxmen1110@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Logan#789'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True