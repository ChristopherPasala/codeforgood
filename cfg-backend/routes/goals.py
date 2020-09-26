from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user_goals import UserGoals
import json

class Goals(Resource):
    def get(self, userid):
        goals = UserGoals.query.filter_by(user_id=userid).all()

        if goals:
            return jsonify({'status': 'ok', 'goals': [{'goalName': goal.goalName, 'goalAmount': goal.goalAmount, 'goalAge': goal.goalAge} for goal in goals]})
        else:
            return jsonify({'status': "User goals not found"})
        
    def post(self, userid):
        args = json.loads(request.data)

        goalName = args['goalName']
        goalAmount = args['goalAmount']
        goalAge = args['goalAge']

        # if UserGoals.query.filter_by(user_id=userid).first() is not None:
        #     return jsonify({'status': "Goals already input"})

        goals = UserGoals(user_id=userid, goalName=goalName, goalAmount=goalAmount, goalAge=goalAge)
        db.session.add(goals)
        db.session.commit()
        return jsonify({'status': 'ok'})