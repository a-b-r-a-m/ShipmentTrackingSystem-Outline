from application import db

class Address(db.Model):
    id = db.Column(db.String(80), unique=True)
    addressRole = db.Column(db.String(80), nullable=False) # enum   
    country = db.Column(db.String(80), nullable=False)
    postCode = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    locality = db.Column(db.String(80), nullable=False) 
    streetName = db.Column(db.String(80))
    streetNr = db.Column(db.String(80))
    streetSufix= db.Column(db.String(80))
    note = db.Column(db.String(120))
    