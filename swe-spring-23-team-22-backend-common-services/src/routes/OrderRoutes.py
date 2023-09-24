import sys
sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

from flask import Blueprint, jsonify, request, session, make_response, Flask
from flask_login import current_user, login_required
from mapbox import Geocoder
import requests
import json
from database import db
from models.Order import Order

order_bp = Blueprint('order_bp', __name__)

# Order model routes
# Get all Orders
@order_bp.route('/orders', methods=['GET'])
@login_required
def get_orders():
    orders = Order.query.filter_by(userID=current_user.userID).all()
    result = []
    for order in orders:
        result.append({
            'orderID': order.orderID,
            'destination': order.destination,
            'pluginType': order.pluginType,
            'suppliesNeeded': order.suppliesNeeded,
            'quantity': order.quantity,
            'orderTotal': order.orderTotal,
            'orderStatus': order.orderStatus
        })
    return jsonify(result)

# Get Order by ID
@order_bp.route('/orders/<int:orderID>', methods=['GET'])
@login_required
def get_order(orderID):
    order = Order.query.filter_by(orderID=orderID, userID=current_user.userID).first_or_404()
    result = {
        'orderID': order.orderID,
        'destination': order.destination,
        'pluginType': order.pluginType,
        'suppliesNeeded': order.suppliesNeeded,
        'quantity': order.quantity,
        'orderTotal': order.orderTotal,
        'orderStatus': order.orderStatus
    }
    return jsonify(result)

# Import the necessary modules
import requests
from flask import jsonify, make_response, request
from flask_login import login_required, current_user
from mapbox import Geocoder

# Create new Order
@order_bp.route('/orders', methods=['POST'])
@login_required
def create_order():
    suppliesNeeded = request.json['suppliesNeeded']
    quantity = request.json['quantity']
    orderTotal = request.json['orderTotal']
    destination = request.json['destination']
    orderStatus = request.json['orderStatus']
    pluginType = request.json['pluginType']
    userID = current_user.userID

    # set up Mapbox geocoder client
    geocoder = Geocoder(access_token='pk.eyJ1IjoiY2FsZWJrcmVzcyIsImEiOiJjbGZtd3RpbTEwZzZkM3lsazRmZ2YzbnZqIn0.inNV2EtdbQI4DvN3Y41Pqg')

    # get destination address from request
    destination = request.json['destination']

    # use Mapbox geocoder to get geocode for destination address
    response = geocoder.forward(destination)
    geocode = response.geojson()['features'][0]['geometry']['coordinates']
    print(geocode)

    # format geocode as tuple
    geocode_tuple = (geocode[1], geocode[0])
    print(geocode_tuple)

    # create Order object
    order = Order(suppliesNeeded=suppliesNeeded, quantity=quantity, orderTotal=orderTotal, 
                  destination=destination, orderStatus=orderStatus, pluginType=pluginType, userID=userID)

    # add Order to SQL DB on Demand side
    db.session.add(order)
    db.session.commit()

    # send Order data to the Supply server
    try:
        supply_data = {
            'orderID': order.orderID,
            'suppliesNeeded': suppliesNeeded,
            'quantity': quantity,
            'destination': geocode_tuple,
            'pluginType': pluginType
        }
        supply_url = 'https://swesupply2023team22.xyz/api/demandAPI/order'
        supply_headers = {
            'Content-Type': 'application/json'
        }
        supply_response = requests.post(supply_url, json=supply_data, headers=supply_headers)
        supply_response.raise_for_status()  # Raise an exception if the request fails
        supply_response_data = supply_response.json()
        print('Supply response data:', supply_response_data)
    except requests.exceptions.RequestException as e:
        print('Error sending order data to Supply server:', e)

    result = {
        'orderId': order.orderID,
        'suppliesNeeded': suppliesNeeded,
        'quantity': quantity,
        'orderTotal': orderTotal,
        'destination': destination,
        'orderStatus': orderStatus,
        'pluginType': pluginType,
        'userId': userID
    }
    response = make_response(jsonify(result), 201)
    response.headers['Location'] = '/orders/{}'.format(order.orderID)
    return response



# Update an Order
@order_bp.route('/orders/<int:orderID>', methods=['PUT'])
@login_required
def update_order(orderID):
    order = Order.query.filter_by(orderID=orderID, userID=current_user.userID).first_or_404()

    order.suppliesNeeded = request.json.get('suppliesNeeded', order.suppliesNeeded)
    order.quantity = request.json.get('quantity', order.quantity)
    order.orderTotal = request.json.get('orderTotal', order.orderTotal)
    order.destination = request.json.get('destination', order.destination)
    order.orderStatus = request.json.get('orderStatus', order.orderStatus)
    pluginType = request.json.get('pluginType')
    userID = current_user.userID
    

    db.session.add(order)
    db.session.commit()

    result = {
        'orderId': order.orderID,
        'suppliesNeeded': order.suppliesNeeded,
        'quantity': order.quantity,
        'orderTotal': order.orderTotal,
        'destination': order.destination,
        'orderStatus': order.orderStatus,
        'pluginType': order.pluginType,
        'userId': order.userID
    }
    return jsonify(result)

# Delete an Order
@order_bp.route('/orders/<int:orderID>', methods=['DELETE'])
@login_required
def delete_order(orderID):
    order = Order.query.filter_by(orderID=orderID, userID=current_user.userID).first_or_404()

    if order.userID != current_user.userID:
        return jsonify({'error': 'Unauthorized access'}), 401

    db.session.delete(order)
    db.session.commit()
    return '', 204

# New routes for populating order history

# Get all orders for the current user
@order_bp.route('/populateHistory', methods=['GET'])
@login_required
def populate_history():
    orders = Order.query.filter_by(userID=current_user.userID).all()
    result = []
    for order in orders:
        result.append({
            'orderID': order.orderID,
            'destination': order.destination,
            'pluginType': order.pluginType,
            'suppliesNeeded': order.suppliesNeeded,
            'quantity': order.quantity,
            'orderTotal': order.orderTotal,
            'orderStatus': order.orderStatus
        })
    return jsonify(result)


# Import the necessary modules
import requests
from flask import jsonify, make_response, request
from flask_login import current_user, login_required
from models.User import User
from models.Order import Order