from app import db

class UserGoals(db.Model):
    __tablename__ = 'userGoals'

    user_id = db.Column(db.String, primary_key=True)
    goalName = db.Column(db.String)
    goalAmount = db.Column(db.Float)
    goalAge = db.Column(db.Integer)
    goalYear = db.Column(db.Integer)