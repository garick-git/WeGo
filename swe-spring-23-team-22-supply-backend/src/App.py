import sys
import os

sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, url_for, redirect, session, jsonify, flash
from flask_login import UserMixin, LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from utils import mongoInteraction as db

# local imports
from routes.fleetManagerRoutes import fleetManagerBP
from routes.renderRoutes import renderBP
from routes.dashboardRoutes import dashboardBP
from api.demandAPI import demandAPIBP
from api.vehicleAPI import vehicleAPIBP
from api.demandHeartBeat import demandHeartBeatAPIBP
from api.vehicleHeartBeat import vehicleHeartBeatAPIBP

# app instance initialization
app = Flask(__name__, template_folder='/home/team22/repos/supply-frontend/src/components', static_folder='/home/team22/repos/supply-frontend/src/static')

# login manager initialization
login_manager = LoginManager(app)
# set the login view for the app
login_manager.login_view = '/login'
# define the user_loader callback
@login_manager.user_loader
def loadUser(userId):
    return db.findFleetManager(str(userId))

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(fleetManagerBP)
app.register_blueprint(renderBP)
app.register_blueprint(demandAPIBP)
app.register_blueprint(vehicleAPIBP)
app.register_blueprint(demandHeartBeatAPIBP)
app.register_blueprint(dashboardBP)
app.register_blueprint(vehicleHeartBeatAPIBP)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
