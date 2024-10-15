# from config import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata=MetaData()
db=SQLAlchemy(metadata=metadata)

#Association table
user_groups = db.Table('user_groups',
                       db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                       db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
                       )

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=True)

    posts = db.relationship('Post', back_populates="user")
    groups = db.relationship('Group', secondary=user_groups,back_populates="users")
    
    serialize_rules = ('-posts.user', '-groups.users')
    @validates('email')
    def checking_email(self, _, email_value):
        if '@' not in email_value:
            raise ValueError('Email should have the @ sign')
        return email_value
    
    # def __repr__(self):
    #     return f'User{self.id}: Username: {self.username} email:{self.email}'
    
class Post(db.Model,SerializerMixin):
    __tablename__ = 'posts'
    
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='posts')
    
    serializer_rules = ('-user.posts',)
    
class Group(db.Model,SerializerMixin):
    __tablename__ = 'groups'
    
    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String)
    
    users = db.relationship('User', secondary=user_groups,back_populates="groups")
    
    serialize_rules = ('-users.groups',)
