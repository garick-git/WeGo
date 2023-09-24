import sys
import os

sys.path.insert(0, '/home/team22/repos/backend-common-services/src')
# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, url_for, redirect, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash


# local imports
from models.User import User
from models.Order import Order
from routes.UserRoutes import user_bp
from routes.OrderRoutes import order_bp
# from routes.VehicleRoutes import vehicle_bp
from routes.RenderRoutes import render_bp
from routes.supply_api import supply_bp
from database import db

# /home/team22/repos/ -> all repos

from sqlalchemy.sql import func

# app instance initialization
app = Flask(__name__, template_folder='/home/team22/repos/frontend-common-services/components', static_folder='/home/team22/repos/frontend-common-services/static')

# login manager initialization
login_manager = LoginManager(app)
# set the login view for the app
login_manager.login_view = '/login'
# define the user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# DB configuration
app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2023Team22!@localhost/team22database'

db.init_app(app)

# register route blueprints
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
# app.register_blueprint(vehicle_bp)
app.register_blueprint(render_bp)
app.register_blueprint(supply_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')