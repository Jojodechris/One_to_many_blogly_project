# models.py file
"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,nullable= False, primary_key=True, autoincrement=True)
    
    first_name = db.Column(db.Text, nullable=False, unique=True)
    last_name = db.Column(db.Text, nullable=False, unique=True)
    image_url = db.Column(db.Text, nullable=False, unique=False)

class Post(db.Model):
    """Post Model for blog posts in the database."""
    __tablename__='posts'
    id = db.Column( db.Integer,nullable= False, primary_key=True, autoincrement=True)
    #auto incrementing integer column
    title = db.Column(db.Text, nullable=False,unique=False)
    content = db.Column(db.Text, nullable=False,unique=False)
    users_id = db.Column (db.Integer,db.ForeignKey('users_id'))


    

    