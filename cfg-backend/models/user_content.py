from app import db
from models.user import User

class UserContent(db.Model):
    __tablename__ = 'user_content'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    user = db.relationship(User, backref='user_content', foreign_keys=[user_id])
    contentText = db.Column(db.String)
    