from application import app

@app.route('/')
def index():
    return 'Welcome to Shipment Tracking System'