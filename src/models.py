import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    comment = relationship('Post', backref='post')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    comment = relationship('Comment', backref='comment')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column (Integer, ForeignKey('post.id'))
    comment_text = Column (String(500), nullable=False)
    user = relationship(User)
    post = relationship(Post)

class Picture(Base):
    __tablename__ = 'picture'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey('post.id'))
    url = Column (String(500), nullable=False)
    post = relationship(Post)

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey('post.id'))
    url = Column (String(500), nullable=False)
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e