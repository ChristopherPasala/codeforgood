from app import db

class UserContent(db.Model):
    __tablename__ = 'userContent'

    contentText = db.Column(db.String)
    user_id = db.Column(db.String, primary_key=True)