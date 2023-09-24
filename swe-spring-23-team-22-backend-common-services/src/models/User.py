import sys
sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

from database import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    userID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    fName = db.Column(db.String(100), nullable=False)
    lName = db.Column(db.String(100), nullable=False)
    # servicesUsed = db.Column(db.ARRAY(db.String(100)))

    def get_id(self):
        return str(self.userID)

    def __repr__(self):
        return '<User %r>' % self.username