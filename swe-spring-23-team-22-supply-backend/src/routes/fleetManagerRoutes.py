import sys
import json
import random
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from flask import Blueprint, jsonify, request, session, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
#from database import db
from models.FleetManager import FleetManager
from utils import mongoInteraction as db

# Define User model blueprint
fleetManagerBP = Blueprint('fleetManagerBP', __name__)

# User model routes
# Get all Fleet Managers
@fleetManagerBP.route('/users')
def getAllFleetManagers():
    fleetManagers = db.getAllFleetmanagers()
    return jsonify([json.loads(json.dumps(FM, default=str)) for FM in fleetManagers])

# Get a user by ID
@fleetManagerBP.route('/users/<int:userID>')
def getFleetManagerByID(fleetManagerID):
    fleetManager = db.findFleetManager(fleetManagerID)

    if fleetManager:
        return jsonify(fleetManager)
    else:
        return jsonify({'message': 'User not found.'})

#  Create a new User
@fleetManagerBP.route('/users', methods=['POST'])
def createFleetManager():
    # Get the request data from the request body
    username = request.json['username']
    password = request.json['password']
    fName = request.json['fName']
    lName = request.json['lName']
    email = request.json['email']

    # Generate a hashed version of the password
    hashedPassword = generate_password_hash(password, method='sha256')

    if db.checkIfFleetManagerExists(username, email):
        return jsonify({'message': 'Username or email already associated with an account'})

    # generate a random 6-digit ID for fleetManagerID
    fleetManagerID = str(random.randint(10000, 99999))

    # check if the ID already exists in the collection
    while db.checkIfFleetManagerExistsById(fleetManagerID):
        # regenerate the ID if it already exists in the collection
        fleetManagerID = str(random.randint(10000, 99999))

    fleetManager = FleetManager(_id=fleetManagerID, email=email, username=username, password=hashedPassword, fName=fName, lName=lName)

    db.insert(fleetManager)

    return jsonify({'message': 'User created successfully'})

# Update a FleetManager
@fleetManagerBP.route('/users/<int:fleetManagerID>', methods=['PUT'])
def updateFleetManager(fleetManagerID):

    data = request.get_json()
    if db.findFleetManager(fleetManagerID):
        db.update(fleetManagerID, data)
        return jsonify(db.findFleetManager(fleetManagerID))
    else:
        return jsonify({'message': 'User not found'})

# Delete a FleetManager
@fleetManagerBP.route('/users/<int:fleetManagerID>', methods=['DELETE'])
def deleteFleetManager(fleetManagerID):

    result = db.findFleetManager(fleetManagerID)
    if result:
        db.delete(result)
        return jsonify({'message': 'User deleted'})
    else:
        return jsonify({'message': 'User not found'})

#update fleetManager
@fleetManagerBP.route('/editUserInfo', methods=['PUT'])
def updateUser():
    user = db.findFleetManager(session["_id"])
    if user:
        data = request.get_json()
        update_data = {}

        if 'fName' in data:
            update_data['fName'] = data['fName']
        if 'lName' in data:
            update_data['lName'] = data['lName']
        if 'username' in data:
            update_data['username'] = data['username']
        if 'email' in data:
            update_data['email'] = data['email']
        if 'password' in data:
            hashed_password = generate_password_hash(data['password'], method='sha256')
            update_data['password'] = hashed_password

        oldFleetManager = FleetManager(user['_id'],
                                       user['email'],
                                       user['username'],
                                       user['password'],
                                       user['fName'],
                                       user['lName'])
        newFleetManager = FleetManager(user['_id'],
                                       update_data['email'],
                                       update_data['username'],
                                       update_data['password'],
                                       update_data['fName'],
                                       update_data['lName'])

        db.update(oldFleetManager, newFleetManager)

        return jsonify({'message': 'User updated successfully.'}), 200
    else:
        return jsonify({'message': 'User not found.'})





