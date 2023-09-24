import sys

sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from flask import Blueprint, jsonify, request
from models.Vehicle import Vehicle
from utils import mongoInteraction as db
import requests
import time

vehicleHeartBeatAPIBP = Blueprint('vehicleHeartBeatAPIBP', __name__)

@vehicleHeartBeatAPIBP.route('/api/vehicleHeartBeat/vehicleArray', methods=['POST'])
def vehicleHeartBeat():

    vehicleArray = request.get_json()['vehicleArray']
    #[
    # {'_id':_id, 'vehicleMakeModel':vehicleMakeModel, 'currOrder':currOrder, 'isAvailable': etc...},
    # {'_id':_id, 'vehicleMakeModel':vehicleMakeModel, 'currOrder':currOrder, 'isAvailable': etc...}
    #]

    for vehicle in vehicleArray:
        newVehicle = Vehicle(vehicle['_id'],vehicle['vehicleMakeModel'],vehicle['currOrderRoutes'],vehicle['status'],vehicle['currLocation'],vehicle['fleetName'],vehicle['inventory'])

        if vehicle is None:
            return jsonify({'error': 'Data not found'}), 404

        if db.findVehicle(vehicle['_id']) is None:
            db.insert(newVehicle)
        else:
            oldVehicle = db.findVehicle(vehicle['_id'])
            oldVehicle = Vehicle(_id=oldVehicle['_id'],
                                 vehicleMakeModel=oldVehicle['vehicleMakeModel'],
                                 currOrderRoutes=oldVehicle['currOrderRoutes'],
                                 status=oldVehicle['status'],
                                 currLocation=oldVehicle['currLocation'],
                                 fleetName=oldVehicle['fleetName'],
                                 inventory=oldVehicle['inventory'])
            db.update(oldVehicle, newVehicle)

    return jsonify({'message':'vehicles added successfully'})

