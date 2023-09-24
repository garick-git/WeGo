import sys
sys.path.insert(0, '/home/team22/repos/vehicle-simulator/src')
from database import vehicles
from flask import Flask, request, Blueprint, jsonify
from time import sleep
from datetime import time
from random import random

# define blueprint
registrationEndpointBP = Blueprint('registrationEndpointBP', __name__)

@registrationEndpointBP.route('/endpoints/registration/registerVehicle', methods=['POST'])
def registerVehicle():
    #collect the data from the POST request
    data = request.get_json()
    #create a new vehicle object
    requestedVehicle = vehicles.find_one({'_id': data['vehicleID']})
    requestedVehicle['fleetName'] = data['fleetName']
    requestedVehicle['status'] = data['status'] 
    #update the vehicle in the database
    vehicles.replace_one({'_id': data['vehicleID']}, requestedVehicle)
    return jsonify({'message': 'Vehicle successfully registered'}, 200)