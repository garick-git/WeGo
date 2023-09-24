# import sys
# sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

# from flask import Blueprint, jsonify, request
# from database import db
# from models.Vehicle import Vehicle

# vehicle_bp = Blueprint('vehicle_bp', __name__)


# # Vehicle mode routes
# # Get all vehicles
# @vehicle_bp.route('/vehicles', methods=['GET'])
# def get_vehicles():
#     vehicles = Vehicle.query.all()
#     vehicle_list = []
#     for vehicle in vehicles:
#         vehicle_data = {
#             'id': vehicle.vehicleID,
#             'make_model': vehicle.vehcicleMakeModel,
#             'destination': vehicle.destination,
#             'is_active': vehicle.isActive,
#             'current_location': vehicle.currLocation,
#             'fleet_manager_id': vehicle.fleetManagerID
#         }
#         vehicle_list.append(vehicle_data)
#     return jsonify(vehicle_list)

# # Get a Vehicle by id
# @vehicle_bp.route('/vehicles/<int:vehicle_id>', methods=['GET'])
# def get_vehicle(vehicle_id):
#     vehicle = Vehicle.query.get(vehicle_id)
#     if vehicle:
#         vehicle_data = {
#             'id': vehicle.vehicleID,
#             'make_model': vehicle.vehcicleMakeModel,
#             'destination': vehicle.destination,
#             'is_active': vehicle.isActive,
#             'current_location': vehicle.currLocation,
#             'fleet_manager_id': vehicle.fleetManagerID
#         }
#         return jsonify(vehicle_data)
#     else:
#         return jsonify({'message': 'Vehicle not found'})

# # Add a Vehicle
# @vehicle_bp.route('/vehicles', methods=['POST'])
# def add_vehicle():
#     vehicle_data = request.get_json()
#     new_vehicle = Vehicle(
#         vehcicleMakeModel=vehicle_data['make_model'],
#         destination=vehicle_data['destination'],
#         isActive=vehicle_data['is_active'],
#         currLocation=vehicle_data['current_location'],
#         fleetManagerID=vehicle_data['fleet_manager_id']
#     )
#     db.session.add(new_vehicle)
#     db.session.commit()
#     return jsonify({'message': 'Vehicle added successfully'})

# # Update a Vehicle
# @vehicle_bp.route('/vehicles/<int:vehicle_id>', methods=['PUT'])
# def update_vehicle(vehicle_id):
#     vehicle = Vehicle.query.get(vehicle_id)
#     if vehicle:
#         vehicle_data = request.get_json()
#         vehicle.vehcicleMakeModel = vehicle_data['make_model']
#         vehicle.destination = vehicle_data['destination']
#         vehicle.isActive = vehicle_data['is_active']
#         vehicle.currLocation = vehicle_data['current_location']
#         vehicle.fleetManagerID = vehicle_data['fleet_manager_id']
#         db.session.commit()
#         return jsonify({'message': 'Vehicle updated successfully'})
#     else:
#         return jsonify({'message': 'Vehicle not found'})

# # Delete a Vehicle
# @vehicle_bp.route('/vehicles/<int:vehicle_id>', methods=['DELETE'])
# def delete_vehicle(vehicle_id):
#     vehicle = Vehicle.query.get(vehicle_id)
#     if vehicle:
#         db.session.delete(vehicle)
#         db.session.commit()
#         return jsonify({'message': 'Vehicle deleted successfully'})
#     else:
#         return jsonify({'message': 'Vehicle not found'})

