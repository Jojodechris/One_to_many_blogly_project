# models.py file
"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

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
    # users_id = db.Column (db.Integer,db.ForeignKey('users.id'))
    users_id = db.Column(db.Integer, ForeignKey('users.id'))  


class Tag(db.Model):
    '''Tag model'''
    __tablename__ ='tags'
    id = db.Column( db.Integer,nullable= False, primary_key=True, autoincrement=True)
    name  = db.Column(db.Text, nullable=False , unique= True )

    posts = db.relationship(
        'Post',
        secondary="posttag",  
        backref="post_tags",  
    )


class PostTag(db.Model):
    '''Join table between post and tag'''
    __tablename__="posttag"
    tags_id = db.Column(db.Integer,db.ForeignKey('tags.id'),primary_key=True)
    posts_id = db.Column( db.Integer,db.ForeignKey("posts.id"),primary_key=True)
 













    

    