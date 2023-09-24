import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

class Vehicle():

    def __init__(self, _id, vehicleMakeModel, currOrderRoutes, status, currLocation, fleetName, inventory):

        self._id = _id
        self.vehicleMakeModel = vehicleMakeModel
        self.currOrderRoutes = currOrderRoutes
        self.status = status
        self.currLocation = currLocation
        self.fleetName = fleetName
        self.inventory = inventory

    ##### SETTERS #####

    def setId(self, _id):
        self._id = _id

    def setVehicleMakeModel(self, vehicleMakeModel):
        self.vehicleMakeModel = vehicleMakeModel

    def setCurrOrderRoutes(self, routeTo, routeBack):
        self.currOrderRoutes = [routeTo, routeBack]

    def setStatus(self, status):
        self.status = status

    def setCurrLocation(self, currLocation):
        self.currLocation = currLocation

    def setFleetName(self, fleetName):
        self.fleetName = fleetName

    def setInventory(self, inventory):
        self.inventory = inventory

    # def setDestination(self, destination):
    #     self.destination = destination

    ##### GETTERS #####

    def getId(self):
        return self._id

    def getVehicleMakeModel(self):
        return self.vehicleMakeModel

    def getCurrOrderRoutes(self):
        return self.currOrderRoutes

    def getStatus(self):
        return self.status

    def getCurrLocation(self):
        return self.currLocation

    def getFleetName(self):
        return self.fleetName

    def getInventory(self):
        return self.inventory

    # def getDestination(self):
    #     return self.destination

    def __str__(self):
        return f"Vehicle ID: {self._id}\nMake and Model: {self.vehicleMakeModel}\nCurrent Order: {self.currOrder}\nIs Available: {self.isAvailable}\nCurrent Location: {self.currLocation}\nFleet Name: {self.fleetName}\nInventory: {self.inventory}"
