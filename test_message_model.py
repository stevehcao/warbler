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
        new_msg = Message(text="Hey", user_id=1)
        db.session.add(new_user)
        db.session.add(new_msg)
        db.session.commit()
        app.config['TESTING'] = True

    def tearDown(self):
        """Do at end of every test."""
        db.session.close()
        db.drop_all()

    def test_create_msg(self):
        """Test for creating adding message to database"""
        found_msg = Message.query.filter_by(user_id=1).first()
        self.assertEqual(found_msg.user_id, 1)

    def test_destroy_msg(self):
        """Test for deleting a message from database"""
        found_msg = Message.query.filter_by(user_id=1).first()
        db.session.delete(found_msg)
        self.assertNotEqual(found_msg.user_id, None)


if __name__ == '__main__':
    unittest.main()