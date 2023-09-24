import sys
sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from database import db
from models.User import User

# Define User model blueprint
user_bp = Blueprint('user_routes', __name__)

# User model routes
# Get all users
@user_bp.route('/users')
def getAllUsers():
    users = User.query.all()
    return jsonify([user.__dict__ for user in users])

# Get a user by ID
@user_bp.route('/users/<int:userID>')
def getUserByID(userID):
    user = User.query.get(userID)
    if user:
        return jsonify(user.__dict__)
    else:
        return jsonify({'message': 'User not found.'})


#  Create a new User
@user_bp.route('/users', methods=['POST'])
def createUser():
    # Get the request data from the request body
    username = request.json['username']
    password = request.json['password']
    fName = request.json['fName']
    lName = request.json['lName']
    email = request.json['email']

    # Generate a hashed version of the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new User object
    new_user = User(username=username, password=hashed_password, fName=fName, lName=lName, email=email)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})

import hashlib

# Update a User
@user_bp.route('/editUserInfo', methods=['PUT'])
@login_required
def update_user(userID):

    user = User.query.get(userID)
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

        oldUser = user(user['userID'],
                                        user['email'],
                                        user['username'],
                                        user['password'],
                                        user['fName'],
                                        user['lName'])
        newUser = user(user['userID'],
                                        update_data['email'],
                                        update_data['username'],
                                        update_data['password'],
                                        update_data['fName'],
                                        update_data['lName'])

        db.update(oldUser, newUser)

        return jsonify({'message': 'User updated successfully.'}), 200
    else:
        return jsonify({'message': 'User not found.'})


# Delete a User
@user_bp.route('/users/<int:userID>', methods=['DELETE'])
@login_required
def delete_user(userID):
    user = User.query.get(userID)
    if user:
        if user == current_user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully.'})
        else:
            return jsonify({'error': 'You do not have permission to delete this user.'}), 401
    else:
        return jsonify({'error': 'User not found.'}), 404
