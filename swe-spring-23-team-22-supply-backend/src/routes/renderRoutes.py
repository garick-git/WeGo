import sys

sys.path.insert(0, '/home/team22/repos/supply-backend/src')

from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify, flash, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from utils import mongoInteraction as db

renderBP = Blueprint('renderBP', __name__)

# Render route for base
@renderBP.route("/")
def index():
    if 'username' in session:
        return render_template('fleet_dashboard.html')
    return render_template('supply_index.html')


@renderBP.route("/signup", methods=["GET"])
def signup():
    # Render the signup page if the request method is GET
    return render_template('fleet_signup.html')

# login render route
@renderBP.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')

        # Check if username exists in the database
        fleetManager = db.findFleetManagerByUsername(username)
        if not fleetManager:
            return jsonify({'error': 'Username or password is incorrect'})

        # Check if password is correct
        if not check_password_hash(fleetManager['password'], password):
            print("User password: ", fleetManager['password'])
            print("Entered password: ", password)
            return jsonify({'error': 'Username or password is incorrect'})

        # Set session username
        session['username'] = username
        session['_id'] = fleetManager['_id']
        print(session)

        return jsonify({'message': 'Login successful'})

    # Render the login page if the request method is GET
    return render_template('supply_index.html')

# logout render route
@renderBP.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('_id', None)

    return redirect(url_for('renderBP.login'))

# Dashboard page render route
@renderBP.route('/dashboard')
def dashboard():
    if 'username' not in session:
        # Fleet Manager is not logged in, redirect to login page
        return redirect(url_for('renderBP.login'))

        # Fleet Manager is logged in, render the dashboard page
    username = session['username']

    return render_template('fleet_dashboard.html', username=username)

@renderBP.route("/forgotPassword", methods=["GET"])
def forgotPassword():
    # Render the Forgot Password page if the request method is GET
    return render_template('settings.html')

@renderBP.route("/settings", methods=["GET"])
def editUserInfo():
    # Render the edit user info page if the request method is GET
    if 'username' not in session:
        # Fleet Manager is not logged in, redirect to login page
        return redirect(url_for('renderBP.login'))

    return render_template('supply_editUserInfo.html')

@renderBP.route('/supplyTrackingPage', methods=["GET"])
def serveSupplyTrackingPage():
    tracking_page_path = '/home/team22/repos/map-services/src/FrontEndMap'
    return send_from_directory(tracking_page_path, 'supplyTrackingPage.js', mimetype='application/javascript')


