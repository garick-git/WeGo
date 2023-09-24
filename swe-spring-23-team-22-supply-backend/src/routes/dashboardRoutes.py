import sys
import json
import os
import random
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from dotenv import load_dotenv
load_dotenv('/home/team22/repos/supply-backend/src/.env')

from api.vehicleAPI import updateVehicleStatus
from models.Vehicle import Vehicle
from utils import mongoInteraction as db
from api import vehicleAPI
from flask import Blueprint, jsonify, request

# Define dashboard blueprint
dashboardBP = Blueprint('dashboardBP', __name__)

@dashboardBP.route('/editVehicle', methods=['PUT'])
def editVehicle():

    newVehicle = request.get_json()
    vehicleID = newVehicle['_id']
    fleetName = newVehicle['fleetName']
    status = newVehicle['status']

    updateVehicleStatus(vehicleID, fleetName, status)

    return jsonify({'message': 'vehicle updated successfully'})

@dashboardBP.route('/populateVehicles', methods=['GET'])
def populateVehicles():
    arrayOfVehicles = db.getAllVehicles()
    return jsonify([json.loads(json.dumps(v, default=str)) for v in arrayOfVehicles])

@dashboardBP.route('/populateAlerts', methods=['GET'])
def populateAlerts():
    arrayOfVehiclesWithAlert = db.getVehiclesWithAlert()
    return jsonify([json.loads(json.dumps(v, default=str)) for v in arrayOfVehiclesWithAlert])

@dashboardBP.route('/accessToken', methods=['GET'])
def mapBoxAccessToken():
    return jsonify({'accessToken': os.getenv('ACCESS_TOKEN')})



