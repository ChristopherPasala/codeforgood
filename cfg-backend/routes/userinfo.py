from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user_info import UserInfo
import json

class Info(Resource):
    def get(self, userid=None):
        need_user = UserInfo.query.filter_by(user_id=userid).first()

        if need_user:
            return jsonify({'status': 'ok', 'gender': need_user.gender, 'ethnicity': need_user.ethnicity, 'age': need_user.age})
        else:
            return jsonify({'status': "User information not found"})
    
    def post(self, userid=None):
        args = json.loads(request.data)
        gender = args['gender']
        ethnicity = args['ethnicity']
        age = args['age']
        info = UserInfo(user_id=userid, gender=gender, ethnicity=ethnicity, age=age)
        db.session.add(info)
        db.session.commit()
        return jsonify({'status': 'ok'})