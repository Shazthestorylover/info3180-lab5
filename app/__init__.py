from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


user = 'shaz'
password = 'shaz123'
database = 'info3180-lab5'
default = "postgresql://%s:%s@localhost/%s" % (user,password,database)


app = Flask(__name__)
app.config['SECRET_KEY'] = "xqJH87skjvakhvauiweuw73ejwyOIJGhcauGSALSAOIHB.au8swolJKJZDSUSDNSDCHUjdsjdiuenhbs7u329236123t532912-9jas;kkujgs"
app.config['SQLALCHEMY_DATABASE_URI'] = default
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
