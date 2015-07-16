# encoding: utf8

import unittest
from app import app, db
from app.models import User
from config import basedir
import os


class LiquidTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_ok(self):
        assert True is not False

    def test_follow(self):
        u1 = User(nickname='John', email='john@example.com')
        u2 = User(nickname='Susan', email='susan@example.com')

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        assert u1.unfollow(u2) is None

        u = u1.follow(u2)
        db.session.add(u)
        db.session.commit()

        assert u1.follow(u2) is None
        assert u1.is_following(u2)
        assert u1.followed.count() == 1
        assert u1.followed.first().nickname == 'Susan'

        assert u2.followers.count() == 1
        assert u2.followers.first().nickname == 'John'

        u = u1.unfollow(u2)
        assert u is not None
        db.session.add(u)
        db.session.commit()
        assert u1.is_following(u2) is False
        assert u1.followed.count() == 0
        assert u2.followers.count() == 0

    def test_follow_posts(self):
        u1 = User(nickname='John', email='john@example.com')
        assert True is not False
