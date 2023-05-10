from application import db

class Party(db.Model):
    id = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(80)) 
    lastName = db.Column(db.String(80))
    companyName = db.Column(db.String(80))
    contacts = "Many to Many"

    