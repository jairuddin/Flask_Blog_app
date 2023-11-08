from flask import Flask 
import os
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'c6778e981d09a3098345009b30a6f653'
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
Login_manager = LoginManager(app)
Login_manager.login_view="login"
Login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from flaskblog import routes


    
    
    
    
    
