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
        db.session.add(new_user)
        db.session.commit()
        app.config['TESTING'] = True

    def tearDown(self):
        """Do at end of every test."""
        db.session.close()
        db.drop_all()

    def test_login(self):
        client = app.test_client()
        result = client.post(
            '/login',
            data=dict(username='ironmike', password='hello123'),
            follow_redirects=True)
        self.assertIn(b'Hello, ironmike!', result.data)

    def test_logout(self):
        client = app.test_client()
        # first you must login
        result = client.post(
            '/login',
            data=dict(username='ironmike', password='hello123'),
            follow_redirects=True)

        result = client.get('/logout', follow_redirects=True)
        # self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have successfully logged out.', result.data)


if __name__ == '__main__':
    unittest.main()