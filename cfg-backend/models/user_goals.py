from app import db
from models.user import User

class UserGoals(db.Model):
    __tablename__ = 'user_goals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    user = db.relationship(User, backref='user_goals', foreign_keys=[user_id])
    goalName = db.Column(db.String)
    goalAmount = db.Column(db.Float)
    goalAge = db.Column(db.Integer)