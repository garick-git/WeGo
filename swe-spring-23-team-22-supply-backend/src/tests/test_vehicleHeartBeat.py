import sys

sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from flask import Blueprint, jsonify, request
from models.Vehicle import Vehicle
from utils import testMongoInteraction as db
import requests
import time
import unittest

class test_vehicleHeartBeat(unittest.TestCase):

    vehicleHeartBeatAPIBP = Blueprint('vehicleHeartBeatAPIBP', __name__)

    #NEED Help with route
    @vehicleHeartBeatAPIBP.route('/api/vehicleHeartBeat/vehicleArray', methods=['POST'])
    def vehicleHeartBeat():

        vehicleArray = request.get_json()['vehicleArray']
        #[
        # {'_id':_id, 'vehicleMakeModel':vehicleMakeModel, 'currOrder':currOrder, '': etc...},
        # {'_id':_id, 'vehicleMakeModel':vehicleMakeModel, 'currOrder':currOrder, 'isAvailable': etc...}
        #]

        for vehicle in vehicleArray:
            vehicleObj = Vehicle(vehicle['_id'],vehicle['vehicleMakeModel'],vehicle['currOrderRoutes'],vehicle['status'],vehicle['currLocation'],vehicle['fleetName'],vehicle['inventory'])

            if vehicle is None:
                return jsonify({'error': 'Data not found'}), 404

            if db.findVehicle(vehicle['_id']) is None:
                db.insert(vehicleObj)
            else:
                db.update(db.findVehicle(vehicle['_id']), vehicleObj)

        return jsonify({'message':'vehicles added successfully'})

if __name__ == '__main__':
    unittest.main()

    