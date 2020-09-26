from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from passlib.apps import custom_app_context as pwd_context
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

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

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

parser = reqparse.RequestParser()
parser.add_argument('task')
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('password1')
parser.add_argument('password2')


class Index(Resource):
  def get(self):
    print("HOME PAGE")


# Sign up
class Signup(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        username = args['username']
        password = args['password']
        print(username, password)
        # check for missing arguments
        if username is None or password is None:
            abort(400)
        # check for existing user
        if User.query.filter_by(username=username).first() is not None:
            abort(400)

        user = User(username = username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()


# Login
class Login(Resource):
    def post(self):
        print("Login")
        args = parser.parse_args()
        print(args)
        username = args['username']
        password = args['password']
        print(username, password)

        if username is None or password is None:
            abort (400)
        
        # Compare against the database


# Update password
class Updatepass(Resource):
    def put(self):
        print("Update Password")
        args = parser.parse_args()
        print(args)
        username = args['username']
        password1 = args['password1']
        password2 = args['password2']
        print(username, password1, password2)

        # Update password for the username


# Delete account
class Delete(Resource):
    def delete(self):
        print("Delete account")
        args = parser.parse_args()
        username = args['username']
        print(username)

        # Delete username entry


# Get User Information
class User(Resource):
    def get(self):
        print("GET USER INFORMATION")
        args = parser.parse_args()
        username = args['username']
        print(username)

        # Pull data from database and return

##
## Actually setup the Api resource routing here
##
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Updatepass, '/updatepass')
api.add_resource(Delete, '/delete')
api.add_resource(User, '/user')
api.add_resource(Index, '/')


if __name__ == '__main__':
    app.run(debug=True)
    newUser = User(email='test3@gmail.com', user_id='testUser3', typee='student3', password='password3', name = 'bob3')
    db.session.add(newUser)
    db.session.commit()




