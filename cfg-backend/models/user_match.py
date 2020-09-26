from app import db
from models.user import User

class UserMatch(db.Model):
    __tablename__="user_matches"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    user = db.relationship(User, backref='user_matches', foreign_keys=[user_id])
    matches = db.Column(db.ARRAY(db.Integer, dimensions=2), default=[])
