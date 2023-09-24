import sys
import queue
import threading
import time
from flask_cors import CORS, cross_origin
from flask import request, jsonify

sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from flask import Blueprint, jsonify
from utils import mongoInteraction as db

demandHeartBeatAPIBP = Blueprint('demandHeartBeatAPIBP', __name__)
CORS(demandHeartBeatAPIBP, origins=["https://www.swe2023team22.xyz"])

#demandHeartBeatQueue = queue.Queue()

@demandHeartBeatAPIBP.route('/api/demandHeartBeat/<string:vehicleID>', methods=['GET'])
def getCurrLocation(vehicleID):
    if vehicleID is None:
        return jsonify({'error': 'Data not found'}), 404

    # commented out for testing purposes
    #currLocation = ("-97.7579406", "30.231722")
    currLocation = db.getVehicleCurrLocation(vehicleID)

    return jsonify({'currLocation' : currLocation})