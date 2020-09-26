from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user import User
import json

# Login
class Login(Resource):
    def post(self):
        print("Login")
        args = json.loads(request.data)
        print(args)
        email = args['email']
        password = args['password']

        if email is None or password is None:
            return jsonify({'status': "bad request"})

        if User.query.filter_by(email=email).first() is None:
            return jsonify({'status': "user doesn't exist"}) 
            
        log_in_user = User.query.filter_by(email=email).first()

        if log_in_user.verify_password(password):
            return jsonify({'status': 'ok', 'name': log_in_user.name, 'user_id': log_in_user.user_id})
        else:
            return jsonify({'status': "login failed"})