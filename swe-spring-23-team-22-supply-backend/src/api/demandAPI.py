import sys
#import threading
#import time
#import queue
#import multiprocessing
from flask_cors import CORS, cross_origin
from threading import Thread

sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from flask import Blueprint, request, jsonify
from models.Vehicle import Vehicle
from models.Fleet import Fleet
from api import vehicleAPI
from utils import mongoInteraction as db

demandAPIBP = Blueprint('demandAPIBP', __name__)
CORS(demandAPIBP, origins=["https://www.swe2023team22.xyz"])

sys.path.insert(0, '/home/team22/repos/map-services/src/BackEndGeocoding')

from GeocodingUtils import getRouteFromGeocodes

# get orders and put them in a queue
@demandAPIBP.route('/api/demandAPI/order', methods=['POST'])
def initialDispatcher():

    order = request.get_json()
    if order is None:
        return jsonify({'error': 'Data not found'}), 404

    print(f"Received POST request with data: {order}")

    # HARDCODED RESPONSE FOR TESTING PURPOSES
    #route = {'test': 'it works'}
    #optimalVehicleID = '12345'

    # find optimal vehicle for the order
    optimalVehicle = getOptimalVehicle(order)
    if optimalVehicle == None:
        # return None if no vehicles available
        return {'route' : None, 'vehicleID' : None}

    currLocation = optimalVehicle['currLocation']
    optimalVehicleID = optimalVehicle['_id']

    # this route will need to change when we put it in the map-services repo
    #print("currLocation:", currLocation)
    #print("destination:", order['destination'])

    routeTo = getRouteFromGeocodes(currLocation, order['destination'])
    #routeTo = [[coord[1], coord[0]] for coord in routeTo]
    routeBack = getRouteFromGeocodes(order['destination'], currLocation)
    #routeBack = [[coord[1], coord[0]] for coord in routeBack]

    # now give vehicleAPI all the information it needs to get the vehicle
    # restocked and to start moving to the location
    inventory = {order['suppliesNeeded'] : order['quantity']}

    def initVehicleMovementAsync():
        vehicleAPI.initVehicleMovement(optimalVehicleID, routeTo, routeBack, inventory)

    # Start a new thread to run the init_vehicle_movement_async function
    thread = Thread(target=initVehicleMovementAsync)
    thread.start()

    # return jsonify(returnDictionary)
    return jsonify({'route' : routeTo, 'vehicleID' : optimalVehicleID}), 200

def getOptimalVehicle(order):

    # get pluginType from order:
    pluginType = order['pluginType']

    # find fleet associated with pluginType
    fleet = db.findFleetByPluginType(pluginType)

    # get list of vehicles in the fleet that are available
    arrayOfAvailableVehiclesInFleet = db.getAvailableVehiclesInFleet(fleet['fleetName'])

    # if this is 0 that means there are no available vehicles, so we return none back
    if len(arrayOfAvailableVehiclesInFleet) == 0:
        return None

    # for now we are considering St. Edward's to be the only restock location
    # so we do not need to compare other restock locations to the destination
    # if we did, the code for that would go here

    # get the optimal vehicle ID
    optimalVehicle = arrayOfAvailableVehiclesInFleet[0]

    return optimalVehicle


