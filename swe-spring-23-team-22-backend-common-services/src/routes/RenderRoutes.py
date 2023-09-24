import sys
sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.User import User
from models.Order import Order
from database import db

render_bp = Blueprint('render_bp', __name__)

# Render route for base
@render_bp.route("/")
@login_required
def index():
    return render_template('demand_services.html')

@render_bp.route("/signup", methods=["GET"])
def signup():
    # Render the signup page if the request method is GET
    return render_template('demand_signup.html')

@render_bp.route("/editUserInfo", methods=["GET"])
def editUserInfo():
    # Render the Edit User Information page if the request method is GET
    return render_template('demand_editUserInfo.html')

@render_bp.route("/login",methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        
        # Check if username exists in the database
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'error': 'Username or password is incorrect'})

        # Check if password is correct
        if not check_password_hash(user.password, password):
            print("User password: ", user.password)
            print("Entered password: ", password)
            return jsonify({'error': 'Username or password is incorrect'})

        # Create flask-login session
        login_user(user)

        return jsonify({'message': 'Login successful'})

    # Render the login page if the request method is GET
    return render_template('demand_index.html')

@render_bp.route('/logout')
@login_required
def logout():
    print('logout fn called')
    # Log user out and redirect to login page
    logout_user()
    return redirect(url_for('render_bp.index'))

# History page render route
@render_bp.route('/history')
@login_required
def history():
    username = current_user.username

    return render_template('demand_history.html', username=username)

# Ordering page render route
@render_bp.route('/order')
@login_required
def order():
    username = current_user.username

    return render_template('demand_ordering.html', username=username)

# Services page render route
@render_bp.route('/services')
@login_required
def services():
    username = current_user.username

    return render_template('demand_services.html', username=username)

