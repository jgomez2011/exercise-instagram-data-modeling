import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Image(Base):
    __tablename__ = "image"
    id = Column(Integer, primary_key = True)
    image_url = Column(String(300), nullable = False)
    
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String(29), nullable = False, unique = True)
    email = Column(String(55), nullable = False, unique = True)
    Password = Column(String(30), nullable = False)

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key = True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship(User)

    image_id = Column(Integer, ForeignKey('image.id'), nullable = False)
    image = relationship(Image)

    like_id = Column(Integer, ForeignKey('like.id'), nullable = False)
    like = relationship(Like)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key = True)
    comment = Column(String(250))

    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship(User)

    post_id = Column(Integer, ForeignKey('post.id'), nullable = False)
    post = relationship(Post)

class Feed(Base):
    __tablename__ = "feed"
    id = Column(Integer, primary_key = True)

    post_id = Column(Integer, ForeignKey('post.id'), nullable = False)
    post = relationship(Post)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e