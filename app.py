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

from routes.login import Login
from routes.signup import Signup

#base = declarative_base()
#engine = sa.create_engine('postgres://team25:team25@localhost:5432/team25')
#engine = sa.create_engine('postgres://dvetallprjyrmp:cb27c642041e9ac18355edcb59d1964de01eaf391555042ed5df0b4f41c782c8@ec2-34-238-26-109.compute-1.amazonaws.com:5432/d6drjb8qk3cd2g')
#base.metadata.bind = engine
#session = orm.scoped_session(orm.sessionmaker())(bind=engine)


# # Update password
# class Updatepass(Resource):
#     def put(self):
#         print("Update Password")
#         args = parser.parse_args()
#         print(args)
#         username = args['username']
#         password1 = args['password1']
#         password2 = args['password2']
#         print(username, password1, password2)

#         # Update password for the username


# # Delete account
# class Delete(Resource):
#     def delete(self):
#         print("Delete account")
#         args = parser.parse_args()
#         username = args['username']
#         print(username)

#         # Delete username entry


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
# api.add_resource(Updatepass, '/updatepass')
# api.add_resource(Delete, '/delete')
# api.add_resource(User, '/user')
# api.add_resource(Index, '/')


if __name__ == '__main__':
    app.run(debug=True)
    newUser = User(email='test3@gmail.com', user_id='testUser3', typee='student3', password='password3', name = 'bob3')
    db.session.add(newUser)
    db.session.commit()




