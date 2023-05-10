from application import db

class Error(db.Model):
    code = db.Column(db.String(80), nullable=False) 
    message = db.Column(db.String(80), nullable=False)
    reason = db.Column(db.String(80))