import unittest
import json
from App import App, db
from models.User import User
# Test "get all Users" route
class TestGetAllUsers(unittest.TestCase):
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

    def test_get_all_users(self):
        # add sample Users to test DB
        user1 = User(username='john_doe', password='1234', fName='John', lName='Doe', email='john@example.com')
        user2 = User(username='jane_doe', password='5678', fName='Jane', lName='Doe', email='jane@example.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        # check for good status return, accurate User count
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

# Test "get User by id" route
class TestGetUserById(unittest.TestCase):
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

    def test_get_user_by_id(self):
        # add sample User to db
        user = User(username='john_doe', password='1234', fName='John', lName='Doe', email='john@example.com')
        db.session.add(user)
        db.session.commit()
        # check that correct User is returned
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['username'], 'john_doe')

# Test "create User" route
class TestCreateUser(unittest.TestCase):
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

    def test_create_user(self):
        # generate User data in JSON format
        data = {'username': 'john_doe', 'password': '1234', 'fName': 'John', 'lName': 'Doe', 'email': 'john@example.com'}
        # check that POST request fires successfully
        response = self.app.post('/users', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'User created successfully')


# Test "update User" route
class TestUpdateUser(unittest.TestCase):
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

    def test_update_user(self):
        # add sample User to temp db
        user = User(username='john_doe', password='1234', fName='John', lName='Doe', email='john@example.com')
        db.session.add(user)
        db.session.commit()
        # update sample User's username
        data = {'username': 'new_username'}
        response = self.app.put('/users/1', data=json.dumps(data), content_type='application/json')
        # check that username has been updated
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['username'], 'new_username')

# Test "delete User" route
class TestDeleteUser(unittest.TestCase):
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

    def test_delete_user(self):
        # add sample User to test db
        user = User(username='john_doe', password='1234', fName='John', lName='Doe', email='john@example.com')
        db.session.add(user)
        db.session.commit()

         # make DELETE request to /users/{id}
        response = self.app.delete(f'/users/{user.id}')

        # check that response is a JSON object with success message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {'message': 'User deleted'})

        # check that User has been deleted from db
        deleted_user = User.query.get(user.id)
        self.assertIsNone(deleted_user)

        # check that trying to get deleted user returns 404
        response = self.app.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, 404)


# Test creating a User that already exists
class TestCreateExistingUser(unittest.TestCase):
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

    def test_create_existing_user(self):
        # add sample User to temp db
        user = User(username='test', password='test', fName='Test', lName='User', email='test@test.com')
        db.session.add(user)
        db.session.commit()
        # attempt to add same User again
        data = {
            'username': 'test',
            'password': 'test',
            'fName': 'Test',
            'lName': 'User',
            'email': 'test@test.com'
        }
        response = self.app.post('/users', json=data)

        # check that response is JSON object with error message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {'message': 'User already exists'})

        # check that User count is still 1
        users = User.query.all()
        self.assertEqual(len(users), 1)

# Test "update User" route for nonexistent User
class TestUpdateNonexistentUser(unittest.TestCase):
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

    def test_update_nonexistent_user(self):
        # make PUT request to /users/{id} w/ updated data for nonexistent User
        data = {'fName': 'Updated'}
        response = self.app.put('/users/999', json=data)

        # check that response is JSON object with error message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {'message': 'User not found'})

        # check that no User has been added to the db
        users = User.query.all()
        self.assertEqual(len(users), 0)

# Test "delete User" route for nonexistent User
class TestDeleteNonexistentUser(unittest.TestCase):
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

    def test_delete_nonexistent_user(self):
        # add sample User to temp db
        user = User(username='test', password='test', fName='Test', lName='User', email='test@test.com')
        db.session.add(user)
        db.session.commit()

        # make DELETE request to /users/{id} for nonexistent User
        response = self.app.delete('/users/999')

        # check that response is JSON object with error message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {'message': 'User not found'})

        # check that no user has been added to/deleted from the database
        users = User.query.all()
        self.assertEqual(len(users), 1)