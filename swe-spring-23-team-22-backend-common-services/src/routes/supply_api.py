import sys
import json
import requests
import time


sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

from flask import Blueprint, jsonify, request
from flask_login import current_user

from database import db
from models.Order import Order

# Define Supply Model blueprint
supply_bp = Blueprint('supply_api', __name__)

@supply_bp.route('/initial_request', methods=['POST'])
def getInitialRoute():
    # Define the API endpoint URL for the supply server
    api_url = 'https://swesupply2023team22.xyz/api/demandAPI/order'

    # Create an instance of the Order model
    order = Order()

    # Define the order to be sent to the supply server
    unique_order = {
        'destination': order.destination,
        'pluginType': order.pluginType,
        'userID': order.userID,
        'suppliesNeeded': order.suppliesNeeded,
        'quantity': order.quantity,
        'orderID': order.orderID
    }

    # Convert the order to JSON format
    order_json = json.dumps(unique_order)

    # Define the headers for the API request
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the API request to the supply server
    response = requests.post(api_url, headers=headers, data=order_json)

    # Check if the API request was successful
    if response.status_code != 200:
        return jsonify({'error': 'Failed to get initial route'}), response.status_code

    # Convert the response to a JSON object
    returnTuple = json.loads(response.text)

    route = returnTuple[0]
    vehicleID = returnTuple[1]

    getCurrLocation(vehicleID, order.destination)

    # Print the route object
    print(route)

    return jsonify({'success': 'Initial route received'}), 200


def getCurrLocation(vehicleID, destination):
    api_url = 'https://swesupply2023team22.xyz/api/demandHeartBeat'

    vehicle_json = json.dumps(vehicleID)

    # Define the headers for the API request
    headers = {
        'Content-Type': 'application/json'
    }

    currLocation = requests.post(api_url + '/' + vehicleID, headers=headers, data=vehicle_json)

    # Check if the API request was successful
    if currLocation.status_code != 200:
        return

    currLocation = json.loads(currLocation.text)

    while currLocation != destination:
        time.sleep(1)
        # Send the API request to the supply server
        currLocation = requests.post(api_url + '/' + vehicleID, headers=headers, data=vehicle_json)

        # Check if the API request was successful
        if currLocation.status_code != 200:
            return

        currLocation = json.loads(currLocation.text)

        # Send response to MapBox to update the vehicle's location
        # TODO: Implement this part
