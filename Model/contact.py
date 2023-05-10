from application import db

class Contact(db.Model):
    type = db.Column(db.String(80), nullable=False) # enum   
    number = db.Column(db.String(80), nullable=False)
