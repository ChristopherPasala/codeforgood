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
        print("TIMELINE CREATION")
        student = UserGoals.query.filter_by(user_id=userid).all()[1]
        curr = UserInfo.query.filter_by(user_id=userid).first()
        est_int_rate = 0.02
        initial_val = 50
        diffage = student.goalAge - curr.age
        amount = student.goalAmount
        timeInterval = []
        finalAmount = initial_val * (1 + est_int_rate/12)**(12 * diffage) #i am so braindead idek if this works
        for i in range(diffage):
            timeInterval.append(finalAmount)
        
        print(timeInterval)
        return timeInterval

        """
        lol = amount/diffage
        timeInterval = []

        for i in range(student.age-curr.age):
            timeInterval.append(amount)
        
        acceptableRange = 2500
        
        while acceptableRange > 0:
            num = random.randrange(24)
            if num % 2 == 0:
                acceptableRange -= num
                timeInterval[randrange(len(timeInterval))] -= num
            else:
                acceptableRange -=num
                timeInterval[randrange(len(timeInterval))] += num

        return jsonify({'interval': timeInterval})
        """