from app import db

class GeneratedTimeline(db.Model):
    __tablename__ = 'generatedTimeline'

    user_id = db.Column(db.String, primary_key=True)
    time = db.Column(db.Float)
    savings = db.Column(db.Float)