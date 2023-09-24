import sys
sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

from database import db

class Order(db.Model):
    __tablename__ = 'order'

    orderID = db.Column(db.Integer, primary_key=True)
    suppliesNeeded = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    orderTotal = db.Column(db.String(300), nullable=False)
    destination = db.Column(db.String(300), nullable=False)
    orderStatus = db.Column(db.String(100), nullable=False)
    pluginType = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.ForeignKey('user.userID'))

    def __repr__(self):
        return '<Order %r>' % self.orderID
