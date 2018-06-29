from app import app, db
from models import User, Message
import unittest


# making a class for test cases
class MyAppIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        # disabling this token
        app.config['WTF_CSRF_ENABLED'] = False
        app.config[
            "SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/warbler_test'
        self.client = app.test_client()
        db.create_all()
        new_user = User(
            username='ironmike',
            email='ironmike@gmail.com',
            password=User.hash_password('hello123'))
        # new_msg = Message(text="Hey Steph Curry", user_id=1)
        db.session.add(new_user)
        # db.session.add(new_msg)
        db.session.commit()
        app.config['TESTING'] = True

    def tearDown(self):
        """Do at end of every test."""
        db.session.close()
        db.drop_all()

    def test_message_show(self):
        client = app.test_client()
        result = client.post(
            '/login',
            data=dict(username='ironmike', password='hello123'),
            follow_redirects=True)
        result = client.post(
            '/users/1/messages',
            data=dict(text='Hey Steph Curry', user_id=1),
            follow_redirects=True)
        self.assertIn(b'Hey Steph Curry', result.data)

    def test_message_delete(self):
        """testing deleting a message"""
        client = app.test_client()
        result = client.post(
            '/login',
            data=dict(username='ironmike', password='hello123'),
            follow_redirects=True)
        result = client.post(
            '/users/1/messages',
            data=dict(text='Hey Steph Curry', user_id=1),
            follow_redirects=True)
        result = client.delete('/users/1/messages/1', follow_redirects=True)
        self.assertNotIn(b'Hey Steph Curry', result.data)
