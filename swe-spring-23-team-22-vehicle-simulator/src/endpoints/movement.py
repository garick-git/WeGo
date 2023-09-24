import sys
from datetime import time
from random import random, randint

sys.path.insert(0, '/home/team22/repos/vehicle-simulator/src')

from time import sleep
from database import vehicles
from flask import Flask, request, Blueprint, jsonify

# define blueprint
movementEndpointBP = Blueprint('movementEndpointBP', __name__)


def makeVehicleTraverseRoute(vehicleID):
    # retrieve the requested vehicle from the database
    requestedVehicle = vehicles.find_one({'_id': vehicleID})

    # iterate through each order route
    for route in requestedVehicle['currOrderRoutes']:
        # traverse each step of the route
        for step in route:
            print(f"Traversing step: {step}")
            # update the vehicle's current location in the database
            requestedVehicle['currLocation'] = step
            vehicles.update_one({'_id': vehicleID}, {'$set': {'currLocation': step}})
            sleep(randint(0,1))

        # if this is the first route, empty the vehicle's inventory
        if (route == requestedVehicle['currOrderRoutes'][0]):
            requestedVehicle['inventory'] = None
            vehicles.update_one({'_id': vehicleID}, {'$set': {'inventory': None}})

        print("finished traversing route")
    #clear the vehicle's current order routes
    requestedVehicle['currOrderRoutes'] = [None,None]
    # update the vehicle's status to available
    requestedVehicle['status'] = 1
    vehicles.update_one({'_id': vehicleID}, {'$set': {'status': 1}})


@movementEndpointBP.route('/endpoints/movement/initVehicleMovement', methods=['POST'])
def initVehicleMovement():
    # retrieve data from the POST request
    data = request.get_json()

    # retrieve the requested vehicle from the database
    vehicleID = data['vehicleID']

    print(f"updating vehicle {vehicleID} and initiating movement")
    requestedVehicle = vehicles.find_one({'_id': vehicleID})
    # check that the vehicle is available
    if (requestedVehicle['status'] != 1):
        return "vehicle is not available"
    # update the vehicle's current order routes and inventory
    requestedVehicle['currOrderRoutes'] = [data["routeTo"], data["routeBack"]]
    requestedVehicle['inventory'] = data['inventory']

    # update the vehicle's status to in progress and save changes to the database
    requestedVehicle['status'] = 2
    vehicles.replace_one({'_id': vehicleID}, requestedVehicle)

    # start the vehicle on its route
    makeVehicleTraverseRoute(vehicleID)
    return jsonify({'message': 'Vehicle movement initiated'}, 200)
