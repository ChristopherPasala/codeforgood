from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user import User
import json

# Sign up
class Signup(Resource):
    def post(self):
        args = json.loads(request.data)
        print(args)
        email = args['email']
        name = args['name']
        password = args['password']
        print(email, password)
        # check for missing arguments
        if email is None or password is None:
            return jsonify({status: "bad request"}), 403
        # check for existing user
        if User.query.filter_by(email=email).first() is not None:
            return jsonify({status: "user already exists"}), 403

        user = User(email=email, name=name)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()