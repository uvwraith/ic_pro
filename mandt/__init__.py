from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

from mandt.main.routes import page_not_found

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

app.secret_key = "edeacda59ac156398eb419c6b1ba496a5b8d0250cbf6f09299"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'jamesmark7772021@gmail.com'
app.config['MAIL_PASSWORD'] = 'yrvfejyiruzsqqgt' #os.environ.get('MAIL_PASSWORD')

admin = Admin(app, name='microblog', template_mode='bootstrap3')

mail = Mail(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

class Others(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    ssn = db.Column(db.String(120), nullable=False)
    accNum = db.Column(db.String(120), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Others, db.session))

mail = Mail(app)
from mandt.main.routes import main
from mandt.portals.routes import portals

app.register_blueprint(main)
app.register_blueprint(portals)