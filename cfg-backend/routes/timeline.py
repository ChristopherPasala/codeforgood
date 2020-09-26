from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user_goals import UserGoals
from models.user_info import UserInfo
import random
from models.user import User

import json

class Timeline(Resource):
    def get(self, userid=None):
        # TODO: Accomodate for all goals
        timeIntervals = []
        print(len(UserGoals.query.filter_by(user_id=userid).all()))
        for i in range(len(UserGoals.query.filter_by(user_id=userid).all())):
            student = UserGoals.query.filter_by(user_id=userid).all()[i]
            curr = UserInfo.query.filter_by(user_id=userid).first()
            est_int_rate = 0.02
            initial_val = 50
            diffage = student.goalAge - curr.age
            amount = student.goalAmount
            finalAmount = initial_val * (1 + est_int_rate/12)**(12 * diffage)
            finalAmount = round(finalAmount, 2)
            finalAmount = finalAmount * (12 * diffage)

            timeIntervals.append(finalAmount)

        # return timeIntervals
        return jsonify({'status': 'ok', 'timeline': timeIntervals})
