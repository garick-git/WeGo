import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from database import vehicles
from database import fleetManagers
from database import fleets
from models.FleetManager import FleetManager
from models.Fleet import Fleet
from models.Vehicle import Vehicle
from models.enums import VehicleStatusEnum

##### INSERTION #####

def insert(obj):

    if isinstance(obj, Vehicle):
        vehicles.insert_one(obj.__dict__)
    elif isinstance(obj, Fleet):
        fleets.insert_one(obj.__dict__)
    elif isinstance(obj, FleetManager):
        fleetManagers.insert_one(obj.__dict__)

##### DELETION ######

def delete(obj):

    if isinstance(obj, Vehicle):
        vehicles.delete_one({'_id':obj.getId()})
    elif isinstance(obj, Fleet):
        fleets.insert_one({'_id':obj.getId()})
    elif isinstance(obj, FleetManager):
        fleetManagers.insert_one({'_id':obj.getId()})

##### UPDATERS ######

def update(obj, newObj):
    if isinstance(obj, Vehicle):
        vehicles.replace_one({'_id':obj.getId()},newObj.__dict__)
    elif isinstance(obj, Fleet):
        fleets.replace_one({'_id':obj.getId()},newObj.__dict__)
    elif isinstance(obj, FleetManager):
        fleetManagers.replace_one({'_id':obj.getId()},newObj.__dict__)

def updateVehicleFleet(_id, fleetName):
    vehicles.update_one({'_id': _id}, {"$set": {'fleetName': fleetName}})

def updateVehicleStatus(_id, status):
    vehicles.update_one({'_id': _id}, {"$set": {'status': status}})

##### FINDERS #####

def findVehicle(_id):
    return vehicles.find_one({'_id':_id})

def findFleetManager(_id):
    return fleetManagers.find_one({'_id':_id})

def findFleetManagerByUsername(username):
    return fleetManagers.find_one({'username':username})

def findFleet(_id):
    return fleets.find_one({'_id':_id})

def findFleetByPluginType(pluginType):
    return fleets.find_one({"pluginType": pluginType})

##### GETTERS #####

def getAllVehicles():
    return list(vehicles.find())

def getAllFleetManagers():
    return list(fleetManagers.find())

def getAvailableVehiclesInFleet(fleetName):
    filter = {'status': 1, 'fleetName': fleetName}
    return list(vehicles.find(filter))

def getVehicleCurrLocation(_id):
    vehicle = findVehicle(_id)
    if vehicle == None:
        return None
    return vehicle['currLocation']

def getFleetManagerPassword(_id):
    return findFleetManager(_id)['password']

def getVehiclesWithAlert():
    filter = {'status': VehicleStatusEnum.EMERGENCY.value}
    return list(vehicles.find(filter))


##### CHECKERS #####

def checkIfFleetManagerExists(username, email):
    result1 = fleetManagers.find_one({"username":username})
    result2 = fleetManagers.find_one({"email":email})

    if result1 == None or result2 == None:
        return False
    else:
        return True

def checkIfFleetManagerExistsById(_id):
    if fleetManagers.find_one({"_id":_id}):
        return True
    else:
        return False
