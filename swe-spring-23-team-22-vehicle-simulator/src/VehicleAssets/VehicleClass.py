import sys
from datetime import time
import importlib

sys.path.insert(0, '/home/team22/repos')
geoCodingUtils = importlib.import_module('map-services.src.BackEndGeocoding.GeocodingUtils')
getRouteFromGeocodes = geoCodingUtils.getRouteFromGeocodes
adressToGeocode = geoCodingUtils.adressToGeocode
#from map_services.src.BackEndGeocoding.GeocodingUtils import getRouteFromGeocodes
#from map_services.src.BackEndGeocoding.GeocodingUtils import adressToGeocode


class Vehicle():
#id,vehicle make,currLocation,
    def __init__(self, _id):
        self._id = _id  # String
        self.vehicleMakeModel = "Sedan"  # hardcoded string, will be changed to enum
        self.currOrderRoutes = [None,None]  # string, will be the route
        self.status = 4  # boolean
        self.currLocation = [-97.753061,30.22897]  #set to steds long and latt
        self.fleetName = None  # String ex: "A" or "B"
        self.inventory = None  # dictionary String : int {'COVID-19':25} or {'BloodA+':5}


    ##### SETTERS #####

    def setId(self, _id):
        self._id = _id

    def setVehicleMakeModel(self, vehicleMakeModel):
        self.vehicleMakeModel = vehicleMakeModel

    def setCurrOrderRoutes(self, orderID):
        self.currOrderRoutes[0] = orderID[0]
        self.currOrderRoutes[1] = orderID[1]


    def setIsAvailable(self, isAvailable):
        self.isAvailable = isAvailable

    def setCurrLocation(self, currLocation):
        self.currLocation = currLocation

    def setFleetId(self, fleetID):
        self.fleetID = fleetID

    def setInventory(self, inventory):
        self.inventory = inventory

    def setOrderId(self, orderID):
        self.orderID = orderID

    def setDestination(self, destination):
        self.destination = destination

    ##### GETTERS #####

    def getId(self):
        return self._id

    def getVehicleMakeModel(self):
        return self.vehicleMakeModel

    def getCurrOrder(self):
        return self.currOrderRoutes

    def getIsAvailable(self):
        return self.isAvailable

    def getCurrLocation(self):
        return self.currLocation

    def getFleetId(self):
        return self.fleetID

    def getInventory(self):
        return self.inventory

    def getOrderId(self):
        return self.orderID

    def getDestination(self):
        return self.destination

    #pre:vehicle is available
    #post:vehicle will traverse route and update currLocation and set isAvaible to true
    def executeRouteWithMultithreading(self):
        if(self.isAvailable == True):
            #set avaivlivlity to false
            self.isAvailable = False;
            for currGeoLocation in self.currOrderRoutes:
                self.currLocation = currGeoLocation
                #wait for 5 seconds
                time.sleep(5)
if __name__ == "__main__":
    v1 = Vehicle("1")
    v1.setCurrOrderRoutes(v1,"12")

