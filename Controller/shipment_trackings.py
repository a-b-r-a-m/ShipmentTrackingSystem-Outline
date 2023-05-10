from flask import request
from application import app, db
from Model.shipment_tracking import ShipmentTracking

@app.route('/shipmentTrackings')
def search_shipment_trackings(orderId=None, trackingCode=None, statuses=None, receiverDotId=None,
                              statusChangeDateDotgte=None, statusChangeDateDotlte=None, offset=0, limit=0):
    
    shipment_trackings = ShipmentTracking.query.all()
    shipment_trackings = ShipmentTracking.query.get_or_400(orderId, trackingCode, statuses, receiverDotId,
                                                    statusChangeDateDotgte,statusChangeDateDotlte, offset, limit)

    output = []
    for st in shipment_trackings:
        st_data = {'orderId' : st.orderId, 'trackingCode' : st.trackingCode} # ...
        output.append(st_data)

    return {"shipment_trackings" : output}


@app.route('/shipmentTrackings', methods = ['POST'])
def create_shipment_tracking():
    st = ShipmentTracking(orderId = request.json['orderId'], trackingCode = request.json['trackingCode']) # ...
    db.session.add(st)
    db.session.commit()

    return {'id' : st.id}


@app.route('/shipmentTrackings/<id>')
def get_shipment_tracking_by_id(id):
    st = ShipmentTracking.query.get_or_404(id)

    return {'orderId' : st.orderId, 'trackingCode' : st.trackingCode}


@app.route('/shipmentTrackings/<id>', methods = ['PATCH'])
def update_shipment_tracking_by_id(id):
    st = ShipmentTracking.query.get_or_404_or_400(id)

    return {'orderId' : st.orderId, 'trackingCode' : st.trackingCode}


@app.route('/shipmentTrackings/<status>')
def get_shipment_tracking_by_status(status):
    shipment_trackings = ShipmentTracking.query.all() # where status == status

    output = []
    for st in shipment_trackings:
        st_data = {'orderId' : st.orderId, 'trackingCode' : st.trackingCode} # ...
        output.append(st_data)

    return {"shipment_trackings" : output}


@app.route('/shipmentTrackings/<tracking_date>')
def get_shipment_tracking_by_tracking_date(tracking_date, fromDate, toDate):
    shipment_trackings = ShipmentTracking.query.all() # where tracking_date >= fromDate and tracking_date <= toDate

    output = []
    for st in shipment_trackings:
        st_data = {'orderId' : st.orderId, 'trackingCode' : st.trackingCode} # ...
        output.append(st_data)

    return {"shipment_trackings" : output}

#TODO check if repository system is used