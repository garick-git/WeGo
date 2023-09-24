import sys

sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from flask import Blueprint, jsonify, request
from models import Vehicle
from utils import mongoInteraction as db
import requests
import time
import json

vehicleAPIBP = Blueprint('vehicleAPIBP', __name__)

# tell VSIM to start moving vehicle
def initVehicleMovement(vehicleID, routeTo, routeBack, inventory):

    """
    vehicle = db.findVehicle(vehicleID)
    vehicleObj = Vehicle(vehicle['_id'], vehicle['vehicleMakeModel'], vehicle['currOrderRoutes'], vehicle['isAvailable'],
                         vehicle['currLocation'], vehicle['fleetName'], vehicle['inventory'])

    vehicleObj.setCurrOrderRoutes(routeTo, routeBack)
    vehicleObj.setInventory(inventory)
    """

    data = {"vehicleID" : vehicleID, "routeTo" : routeTo, "routeBack" : routeBack, "inventory" : inventory}

    jsonData = json.dumps(data)

    headers = {
        'Content-Type' : 'application/json'
    }

    response = requests.post("http://45.55.32.208/endpoints/movement/initVehicleMovement", headers=headers, data=jsonData)

    if response.status_code == 200:
        print(f'Request successful with status code {response.status_code}')
    else:
        print(f'Request failed with status code {response.status_code}')

def updateVehicleStatus(vehicleID, fleetName, status):

    data = {"vehicleID" : vehicleID, "fleetName" : fleetName, "status" : status}

    jsonData = json.dumps(data)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post("http://45.55.32.208/endpoints/registration/registerVehicle", headers=headers, data=jsonData)

    if response.status_code == 200:
        print(f'Request successful with status code {response.status_code}')
    else:
        print(f'Request failed with status code {response.status_code}')