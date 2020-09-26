from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
import sqlalchemy as sa

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dvetallprjyrmp:cb27c642041e9ac18355edcb59d1964de01eaf391555042ed5df0b4f41c782c8@ec2-34-238-26-109.compute-1.amazonaws.com:5432/d6drjb8qk3cd2g'
db = SQLAlchemy(app)

#base = declarative_base()
#engine = sa.create_engine('postgres://team25:team25@localhost:5432/team25')
#engine = sa.create_engine('postgres://dvetallprjyrmp:cb27c642041e9ac18355edcb59d1964de01eaf391555042ed5df0b4f41c782c8@ec2-34-238-26-109.compute-1.amazonaws.com:5432/d6drjb8qk3cd2g')
#base.metadata.bind = engine
#session = orm.scoped_session(orm.sessionmaker())(bind=engine)


class User(db.Model):
    __tablename__ = 'users'

    email = Column(String)
    user_id = Column(String, primary_key=True)
    typee = Column(String)
    password = Column(String)
    name = Column(String)

class UserGoals(db.Model):
    __tablename__ = 'userGoals'

    user_id = Column(String, primary_key=True)
    goalName = Column(String)
    goalAmount = Column(Float)
    goalAge = Column(Integer)
    goalYear = Column(Integer)

class UserContent(db.Model):
    __tablename__ = 'userContent'

    contentText = Column(String)
    user_id = Column(String, primary_key=True)

class GeneratedTimeline(db.Model):
    __tablename__ = 'generatedTimeline'

    user_id = Column(String, primary_key=True)
    time = Column(Float)
    savings = Column(Float)

class Index(Resource):
  def get(self):
    print("HOME PAGE")

api.add_resource(Index, '/')
if __name__ == '__main__':
    app.run(debug=True)
    newUser = User(email='test3@gmail.com', user_id='testUser3', typee='student3', password='password3', name = 'bob3')
    db.session.add(newUser)
    db.session.commit()




