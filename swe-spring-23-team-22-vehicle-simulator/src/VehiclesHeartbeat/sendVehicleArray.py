import sys
sys.path.insert(0, '/home/team22/repos')
import threading
from time import sleep
import requests
from flask import json, jsonify
import importlib

database = importlib.import_module('vehicle-simulator.src.database')
vehicles = database.vehicles

geoCodingUtils = importlib.import_module('map-services.src.BackEndGeocoding.GeocodingUtils')
getRouteFromGeocodes = geoCodingUtils.getRouteFromGeocodes
adressToGeocode = geoCodingUtils.adressToGeocode

VehicleClass = importlib.import_module('vehicle-simulator.src.VehicleAssets.VehicleClass')
Vehicle = VehicleClass.Vehicle

#from map_services.src.BackEndGeocoding.GeocodingUtils import getRouteFromGeocodes
#from map_services.src.BackEndGeocoding.GeocodingUtils import adressToGeocode
#from vehicle_simulator.src.VehicleAssets.VehicleClass import Vehicle
vehicle_array_api = 'https://swesupply2023team22.xyz/api/vehicleHeartBeat/vehicleArray'
HEARTBEAT_INTERVAL = 1.49

class VehicleSimulator:

    def __init__(self):
      #fetch vehicles from vehicleCollection
        if(len(list(vehicles.find())) == 0):
            for i in range(1,6):
                self.addVehicleToDB()
        else:
            print(f"Vehicles already in DB with a total of {len(list(vehicles.find()))} vehicles")
        self.running = True
        self.heartBeat()
    def heartBeat(self):
        if(self.running== False):
            print("you goofed up")
        else:
            while self.running:
                data = json.dumps({'vehicleArray':list(vehicles.find())})#sends vehicle array to vehicle_array_api
                headers = {
                    'Content-Type': 'application/json'
                }
                response = requests.post(vehicle_array_api, headers=headers, data=data)
                if response.status_code != 200:
                    print(jsonify({'error': 'Failed to get initial route'}), response.status_code)
                else:
                    print("Sent vehicle array to vehicle_array_api")
                sleep(HEARTBEAT_INTERVAL)

    def setRouteForSpecificVehicle(self, vehicleID, p_adressToRouteTo, p_adressToRouteFrom):
        adressToRouteTo = getRouteFromGeocodes(adressToGeocode(p_adressToRouteFrom), adressToGeocode(p_adressToRouteTo))
        adressToRouteFrom = getRouteFromGeocodes(adressToGeocode(p_adressToRouteTo), adressToGeocode(p_adressToRouteFrom))
        vehicleArray = list(vehicles.find())
        for vehicle in vehicleArray:
            if vehicle['_id'] == vehicleID:
                vehicle['currOrderRoutes'] = [adressToRouteTo, adressToRouteFrom]
                break
        return vehicleArray







    def addVehicleToDB(self):
        vehicleCount = len(list(vehicles.find()))+1
        vehicleObject = Vehicle(str(vehicleCount))
        vehicles.insert_one(vehicleObject.__dict__)


    def toStringVehicle(self):
        vehicleArray = list(vehicles.find())
        for vehicle in vehicleArray:
            print("VehicleID: " + str(vehicle['_id']))
            print("currLocation: " + str(vehicle['currLocation']))
            print("currOrderRoutes: " + str(vehicle['currOrderRoutes']))
            print("available: " + str(vehicle['available']))
            print("inventory: " + str(vehicle['inventory']))
            print("status: " + str(vehicle['status']))

    def killHeartBeat(self):
        self.running = False
        print("Killed heartbeat and the status of running is: " + str(self.running))

if __name__ == '__main__':
    sim1 = VehicleSimulator()
    while True:
        print("Enter 1 to send vehicle array to vehicle_array_api")
        print("Enter 2 to set a route for a specific vehicle")
        print("Enter 3 to make a vehicle execute a route")
        print("enter 4 to print vehicle array")
        print("Enter 5 to exit")
        user_input = int(input("Enter input:"))
        if user_input == 1:
            sim1.sendVehicleArrayTovehicle_array_api(sim1.vehicleArray)
        elif user_input == 2:
            vehicleID = input("Enter vehicleID: ")
            adressToRouteTo = input("Enter adress to route to: ")
            adressToRouteFrom = input("Enter adress to route from: ")
            sim1.vehicleArray = sim1.setRouteForSpecificVehicle( vehicleID, adressToRouteTo, adressToRouteFrom)
        elif user_input == 3:
            vehicleID = input("Enter vehicleID: ")
            vehicleArray = sim1.makeVehicleTraverseRoute(vehicleID)
        elif user_input == 4:
            sim1.printVehicleArrayWithForloop()
        elif user_input == 5:
            break
#"1647 Post Road, San Marcos, TX"),adressToGeocode("908 Paseo De castana way,leander,TX")