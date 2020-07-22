from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SECRET_KEY'] = '71675c0e444e6f197b174b9ea48a9c71'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from flaskblog import routes