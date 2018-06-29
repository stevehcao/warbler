from app import app, db
from models import User, Message
import unittest


# making a class for test cases
class MyAppIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        app.config[
            "SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/warbler_test'
        self.client = app.test_client()
        db.create_all()
        new_user = User(
            username='ironmike', email='ironmike@gmail.com', password='hello')
        db.session.add(new_user)
        db.session.commit()
        app.config['TESTING'] = True

    def tearDown(self):
        """Do at end of every test."""
        db.session.close()
        db.drop_all()

    def test_create_user(self):
        found_user = User.query.filter_by(username='ironmike').first()
        self.assertEqual(found_user.username, 'ironmike')

    def test_delete_user(self):
        found_user = User.query.filter(User.id == 1).first()
        db.session.delete(found_user)
        db.session.commit()
        self.assertNotEqual(found_user, None)

    # def test_login(self):
    #     client = app.test_client()
    #     result = client.post(
    #         '/login',
    #         data=dict(username='ironmike', password='hello'),
    #         follow_redirects=True)
    #     self.assertEqual(b'Hello, ironmike', result.data)


if __name__ == '__main__':
    unittest.main()