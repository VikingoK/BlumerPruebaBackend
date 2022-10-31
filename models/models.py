from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config import Base

class Post(Base):
    __tablename__="posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    video_url = Column(String)
    created_at = Column(String)
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__="comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    created_at = Column(String)
    post_id =  Column(Integer, ForeignKey("posts.id"), nullable=False)
    post = relationship("Post", back_populates="comments")
