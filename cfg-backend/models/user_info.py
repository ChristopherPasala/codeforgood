from app import db
from models.user import User

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    user = db.relationship(User, backref='user_info', foreign_keys=[user_id])
    ethnicity = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)