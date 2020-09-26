from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import orm
from passlib.apps import custom_app_context as pwd_context
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from seed import seed_app

@app.cli.command()
def seed():
    seed_app()


from routes.login import Login
from routes.signup import Signup
from routes.match import Match
from routes.userinfo import Info
from routes.usercont import Content
from routes.goals import Goals
from routes.timeline import Timeline

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

##
## Actually setup the Api resource routing here
##
api.add_resource(Signup, '/api/signup')
api.add_resource(Login, '/api/login')
api.add_resource(Info, '/api/user/<userid>')
api.add_resource(Match, '/api/match/<userid>')
# api.add_resource(Content, '/usercont/<userid>')
api.add_resource(Goals, '/api/goals/<userid>')
api.add_resource(Timeline, '/api/timeline/<userid>')


if __name__ == '__main__':
    app.run(debug=True)
    # newUser = User(email='test3@gmail.com', user_id='testUser3', typee='student3', password='password3', name = 'bob3')
    # db.session.add(newUser)
    # db.session.commit()
