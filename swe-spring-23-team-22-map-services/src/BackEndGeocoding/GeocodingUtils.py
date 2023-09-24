import random
import mapbox
import polyline
import json
import requests
import time
# Mapbox API access token
access_token = 'pk.eyJ1IjoibXNjeWhldiIsImEiOiJjbGRjZ2NxMWcwNHlqM3Ftdnk5bWxpNTA2In0.eVb9A1KnXMC8RXlJjetGpw'


# pre:enter a valid address mapbox will recognise
# post:returnns the geocode to said address
def adressToGeocode(address):
    geocode = None
    # address = "1647 Post Road, San Marcos, TX"  # requested address
    # creates URL(api call) to mapbox that requests information about the requested address
    geocoding_url = (f"https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={access_token}")
    # fire the URL(api call) to mapbox with GET request
    geocodeRequest = requests.get(geocoding_url)
    # format text into json object
    dictionary = json.loads(geocodeRequest.text)
    # select the first features dictionary which contains geocode for location
    geocode = dictionary['features'][0]['geometry']['coordinates']
    if(geocode == None):
        print("INVALID ADDRESS SENT PLEASE RECHECK INPUTS FOR PROPER ADDRESS")
    return geocode


# pre:two correct geocodes for starting and ending position
# post:returns the route which contains the list of geocodes
def getRouteFromGeocodes(startingCoordinate, endingCoordinate):
    route = None
    #format the url(the api call) with requested coordinates

    direction_url = f'https://api.mapbox.com/directions/v5/mapbox/driving/{startingCoordinate[0]},{startingCoordinate[1]};{endingCoordinate[0]},{endingCoordinate[1]}?geometries=geojson&overview=full&access_token={access_token}'#update
    print(direction_url)
    #fire the requested data at the server with a GET request
    request = requests.get(direction_url)
    #format text into JSON
    formatedData = json.loads(request.text)
    #parse through JSON to get the geometry code(compressed list of geocodes aka the route)
    route = formatedData['routes'][0]['geometry']['coordinates']
    print(route)
    return route


# grab the requested vehicle address initial location
# grab the desired destination
# print step by step geocode route
# reloop

#test calls
if __name__ == '__main__':
    # print(getRouteFromGeocodes(adressToGeocode("1647 Post Road, San Marcos, TX"),adressToGeocode("908 Paseo De castana way,leander,TX")))
    route = getRouteFromGeocodes(adressToGeocode("1647 Post Road, San Marcos, TX"),
                                 adressToGeocode("3001 S congress Ave,Austin,TX"))
    print(route)
