import unittest
import json
from App import App, db
from models.Order import Order
# Test "get all Orders" route
class TestGetAllOrders(unittest.TestCase):
    # setup temp db
    def setUp(self):
        App.config['TESTING']  = True
        App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()
        self.app = App.test_client()
    # teardown temp db
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_orders(self):
        # add sample Users to test DB
        order1 = Order(suppliesNeeded='Coronavirus', quantity=100, orderTotal='$1200', destination='100 Test Street', orderStatus='In progress', userID=1)
        order2 = Order(suppliesNeeded='Measles', quantity=10, orderTotal='$200', destination='100 Test Street', orderStatus='In progress', userID=2)
        db.session.add(order1)
        db.session.add(order2)
        db.session.commit()
        # check for good status return, accurate Order count
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)