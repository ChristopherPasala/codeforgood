from sqlalchemy import create_engine
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
import sqlalchemy as sa

base = declarative_base()
#engine = sa.create_engine('postgres://rxrqggyvnlgnra:a4fe0d9cffd7738f9b8c7d225c6b66d53c866ae7c5af9fe1db7dcc5c280e0cd7@ec2-54-160-120-28.compute-1.amazonaws.com:5432/d4c6i9kmtu9s3l')
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)


class User(base):
    __tablename__ = 'users'

    email = Column(String)
    user_id = Column(String, primary_key=True)
    typee = Column(String)
    password = Column(String)
    name = Column(String)

class userGoals(base):
    __tablename__ = 'userGoals'

    user_id = Column(String, primary_key=True)
    goalName = Column(String)
    goalAmount = Column(Float)
    goalAge = Column(Integer)
    goalYear = Column(Integer)

class userContent(base):
    __tablename__ = 'userContent'

    contentText = Column(String)
    user_id = Column(String, primary_key=True)

class generatedTimeline(base):
    user_id = Column(String, primary_key=True)
    time = Column(Float)
    savings = Column(Float)


newUser = User(email='test@gmail.com', user_id='testUser', typee='student', password='password', name = 'bob')
session.add(newUser)
session.commit()

