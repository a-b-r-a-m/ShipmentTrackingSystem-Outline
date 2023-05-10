from application import db

class ShipmentTracking(db.Model):
    id = db.Column(db.String(80), unique=True)
    orderId = db.Column(db.String(80), nullable=False)
    carrier = db.Column(db.String(80))
    trackingCode = db.Column(db.String(80))
    carrierTrackingUrl = db.Column(db.String(80))
    trackingDate = db.Column(db.String(80)) # date-time
    status = db.Column(db.String(80)) # enum
    statusReason = db.Column(db.String(120))
    statusChangeDate = db.Column(db.String(80)) # date-time
    weight = db.Column(db.Integer)
    estimatedDeliveryDate = db.Column(db.String(80)) # date-time
    sender = 'Many to 1 Party, NotNull'
    receiver = 'Many to 1 Party, NotNull'
    addressFrom = 'Many to 1 Address, NotNull'
    addressTo = 'Many to 1 Address, NotNull'

    # def __repr__(self) -> str:
    #     return f"{self.name} - {self.description}"