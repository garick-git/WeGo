import sys
sys.path.insert(0, '/home/team22/repos/backend-common-services/src')

import unittest
from database import db
from models import User


class userTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testUserDB')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user = User(
            email='testemail@gmail.com',
            username='testuser',
            password='T3st!@#$',
            fName='Taha',
            lName='Lewis'
        )
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def testUser(self):
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'testemail@gmail.com')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'T3st!@#$')
        self.assertEqual(user.fName, 'Taha')
        self.assertEqual(user.lName, 'Lewis')


if __name__ == '__main__':
    unittest.main()