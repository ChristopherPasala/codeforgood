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

##
## Actually setup the Api resource routing here
##
api.add_resource(Signup, '/api/signup')
api.add_resource(Login, '/api/login')
api.add_resource(Info, '/api/user/<userid>')
api.add_resource(Match, '/api/match/<userid>')
api.add_resource(Goals, '/api/goals/<userid>')
api.add_resource(Timeline, '/api/timeline/<userid>')


if __name__ == '__main__':
    app.run(debug=True)
