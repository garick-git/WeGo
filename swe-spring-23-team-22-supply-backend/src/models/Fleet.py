import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

class Fleet:
    def __init__(self, _id, fleetName, pluginType, restockLocation):
        self._id = _id
        self.fleetName = fleetName
        self.pluginType = pluginType
        self.restockLocation = restockLocation

    ##### SETTERS #####

    def setId(self, _id):
        self._id = _id

    def setFleetName(self, fleetName):
        self.fleetName = fleetName

    def setPluginType(self, pluginType):
        self.pluginType = pluginType

    def setRestockLocation(self, restockLocation):
        self.restockLocation = restockLocation

    ##### GETTERS #####

    def getId(self):
        return self._id

    def getFleetName(self):
        return self.fleetName

    def getPluginType(self):
        return self.pluginType

    def getRestockLocation(self):
        return self.restockLocation

    def __str__(self):
        return f"Fleet ID: {self._id}\nFleet Name: {self.fleetName}\nPlugin Type: {self.pluginType}\nRestock Location: {self.restockLocation}"
