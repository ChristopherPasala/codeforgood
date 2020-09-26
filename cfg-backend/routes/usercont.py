from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user_content import UserContent
import json

class Content(Resource):
    def get(self, userid):
        print("GET USER CONTENT")
        need_user = UserContent.query.filter_by(user_id=userid).first()

        if need_user:
            return jsonify({'contentText': need_user['contentText']})
        else:
            return jsonify({'status': "No user content found"})

    # def post(self, userid):
    #     print("UPLOAD NEW USER CONTENT")