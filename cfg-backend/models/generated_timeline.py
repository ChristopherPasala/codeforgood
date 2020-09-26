from app import db
from models.user import User

class GeneratedTimeline(db.Model):
    __tablename__ = 'generated_timeline'
    id = db.Column(db.Column, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    user = db.relationship(User, backref='generated_timeline', foreign_keys=[user_id])
    time = db.Column(db.Float)
    savings = db.Column(db.Float)