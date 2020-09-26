from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user import User
import json

# Get User Information
class Userdata(Resource):
    def get(self, userid):
        print("GET USER INFORMATION")

        need_user = User.query.filter_by(user_id=userid).first()

        if need_user:
            return jsonify({'user_id': need_user.user_id, 'name': need_user.name, 'email': need_user.email})
        else:
            return jsonify({'status': "User information not found"})

        # Pull data from database and return