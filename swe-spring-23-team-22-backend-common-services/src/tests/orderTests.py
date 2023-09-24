import unittest
from database import db
from models import Order
sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

class orderTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testOrderDB')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.order = Order(
            suppliesNeeded='COVID',
            quantity=10,
            orderTotal='900.00',
            destination='4123 Birdwatch Loop, Pflugerville, TX, USA',
            orderStatus='In Progress',
            pluginType=1,
            userID=23
        )
        db.session.add(self.order)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def testOrder(self):
        order = Order.query.filter_by(suppliesNeeded='COVID').first()
        self.assertIsNotNone(order)
        self.assertEqual(order.quantity, 10)
        self.assertEqual(order.suppliesNeeded, 'COVID')
        self.assertEqual(order.orderTotal, '900.00')
        self.assertEqual(order.destination, '4123 Birdwatch Loop, Pflugerville, TX, USA')
        self.assertEqual(order.orderStatus, 'In Progress')
        self.assertEqual(order.pluginType, 1)
        self.assertEqual(order.userID, 23)


if __name__ == '__main__':
    unittest.main()