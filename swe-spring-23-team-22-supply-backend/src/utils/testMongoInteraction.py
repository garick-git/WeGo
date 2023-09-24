import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from database import testVehicles
from database import testFleetManagers
from database import testFleets
from models.FleetManager import FleetManager
from models.Fleet import Fleet
from models.Vehicle import Vehicle
from models.enums import VehicleStatusEnum

##### INSERTION #####

def insert(obj):

    if isinstance(obj, Vehicle):
        testVehicles.insert_one(obj.__dict__)
    elif isinstance(obj, Fleet):
        testFleets.insert_one(obj.__dict__)
    elif isinstance(obj, FleetManager):
        testFleetManagers.insert_one(obj.__dict__)

##### DELETION ######

def delete(obj):

    if isinstance(obj, Vehicle):
        testVehicles.delete_one({'_id':obj.getId()})
    elif isinstance(obj, Fleet):
        testFleets.insert_one({'_id':obj.getId()})
    elif isinstance(obj, FleetManager):
        testFleetManagers.insert_one({'_id':obj.getId()})

##### UPDATERS ######

def update(obj, newObj):
    if isinstance(obj, Vehicle):
        testVehicles.replace_one({'_id':obj.getId()},newObj.__dict__)
    elif isinstance(obj, Fleet):
        testFleets.replace_one({'_id':obj.getId()},newObj.__dict__)
    elif isinstance(obj, FleetManager):
        testFleetManagers.replace_one({'_id':obj.getId()},newObj.__dict__)

def updateVehicleFleet(_id, fleetName):
    testVehicles.update_one({'_id': _id, "$set": {'fleetName': fleetName}})

def updateVehicleStatus(_id, status):
    testVehicles.update_one({'_id': _id, "$set": {'status': status}})

##### FINDERS #####

def findVehicle(_id):
    return testVehicles.find_one({'_id':_id})

def findFleetManager(_id):
    return testFleetManagers.find_one({'_id':_id})

def findFleetManagerByUsername(username):
    return testFleetManagers.find_one({'username':username})

def findFleet(_id):
    return testFleets.find_one({'_id':_id})

def findFleetByPluginType(pluginType):
    return testFleets.find_one({"pluginType": pluginType})

##### GETTERS #####

def getAllVehicles():
    return list(testVehicles.find())

def getAllFleetManagers():
    return list(testFleetManagers.find())

def getAvailableVehiclesInFleet(fleetName):
    filter = {'status': 1, 'fleetName': fleetName}
    return list(testVehicles.find(filter))

def getVehicleCurrLocation(_id):
    vehicle = findVehicle(_id)
    return vehicle['currLocation']

def getFleetManagerPassword(_id):
    return findFleetManager(_id)['password']

def getVehiclesWithAlert():
    filter = {'status': VehicleStatusEnum.EMERGENCY}
    return list(testVehicles.find(filter))


##### CHECKERS #####

def checkIfFleetManagerExists(username, email):
    result1 = testFleetManagers.find_one({"username":username})
    result2 = testFleetManagers.find_one({"email":email})

    if result1 == None or result2 == None:
        return False
    else:
        return True

def checkIfFleetManagerExistsById(_id):
    if testFleetManagers.find_one({"_id":_id}):
        return True
    else:
        return False
