import sys
import os

sys.path.insert(0, '/home/team22/repos/vehicle-simulator/src')

from flask import Flask
from endpoints.movement import movementEndpointBP
from endpoints.registration import registrationEndpointBP
# local imports

# app instance initialization
app = Flask(__name__)

app.config['SECRET_KEY'] = 'SuperSecretKey'

app.register_blueprint(movementEndpointBP)
app.register_blueprint(registrationEndpointBP)
if __name__ == "__main__":
    app.run(host='0.0.0.0')