from app import db
from flask import request, jsonify
from flask_restful import Resource
from models.user import User
import json

from models.user_match import UserMatch
from models.user_goals import UserGoals
from models.user_info import UserInfo
from models.user import User

def generate_matches(user_id):
    # gets matched with themselves
    # TODO: update db after matches found
    high_matches = []
    mid_matches = []
    low_matches = []
    matches = []

    student = UserInfo.query.filter_by(user_id=user_id).first()
    count = 0
    for row in UserInfo.query.limit(100).all():
        if(student.ethnicity == row.ethnicity and student.age == row.age and student.gender == row.gender and not(student.user_id == row.user_id)): #is this age current age or later age?
            matches.append({row.user.name})
            count += 1
        if count > 2:
            break

    count = 0
    for row in UserInfo.query.limit(100).all():
        if(student.ethnicity == row.ethnicity and student.age == row.age and not(student.user_id == row.user_id)): #is this age current age or later age?
            matches.append(row.user.name)
            count += 1
        if count > 2:
            break

    count = 0
    for row in UserInfo.query.limit(100).all():
        if(student.ethnicity == row.ethnicity and not(student.user_id == row.user_id)): #is this age current age or later age?
            matches.append(row.user.name)
            count += 1
        if count > 2:
            break

    print(matches)
    return matches

# Update password
class Match(Resource):
    def get(self, userid):
        # args = json.loads(request.data)
        # user_id = args['user_id']
        matches = UserMatch.query.filter_by(user_id=userid).first()
        if not matches:
            matches = generate_matches(userid)
        else:
            matches = matches.matches

        # Putting the match into the database so that we don't find matches each time
        # match = UserMatch(matches=matches)
        # db.session.add(match)
        # db.session.commit()

        return jsonify({"matches": matches})
        # Update password for the username
