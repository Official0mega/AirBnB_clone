#!/usr/bin/python3
"""
Module for testing DBStorage.
"""
import os
import unittest
from datetime import datetime
import MySQLdb

from models import storage
from models.user import User
from models.engine.db_storage import DBStorage


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
class TestDBStorage(unittest.TestCase):
    """
    Class to test the database storage method.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # Create a new user for testing
        self.new_user = User(
            email='john2020@gmail.com',
            password='password',
            first_name='John',
            last_name='Zoldyck'
        )
        self.new_user.save()

    def tearDown(self):
        """
        Clean up after each test.
        """
        # Delete the user from the database
        self.new_user.delete()

    def test_new(self):
        """
        Test that a new object is correctly added to the database.
        """
        self.assertTrue(self.new_user in storage.all().values())
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(self.new_user.id))
        result = cursor.fetchone()
        cursor.close()
        dbc.close()
        self.assertTrue(result is not None)
        self.assertIn('john2020@gmail.com', result)
        self.assertIn('password', result)
        self.assertIn('John', result)
        self.assertIn('Zoldyck', result)

    def test_delete(self):
        """
        Test that an object is correctly deleted from the database.
        """
        obj_key = 'User.{}'.format(self.new_user.id)
        self.assertTrue(self.new_user in storage.all().values())
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(self.new_user.id))
        result = cursor.fetchone()
        cursor.close()
        dbc.close()
        self.assertTrue(result is not None)
        self.assertIn('john2020@gmail.com', result)
        self.assertIn('password', result)
        self.assertIn('John', result)
        self.assertIn('Zoldyck', result)
        self.assertIn(obj_key, storage.all(User).keys())
        self.new_user.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())

    def test_reload(self):
        """
        Test the reloading of the database session.
        """
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
            [
                '4447-by-me',
                str(datetime.now()),
                str(datetime.now()),
                'ben_pike@yahoo.com',
                'pass',
                'Benjamin',
                'Pike',
            ]
        )
        dbc.commit()
        cursor.close()
        dbc.close()

        self.assertNotIn('User.4447-by-me', storage.all())
        storage.reload()
        self.assertIn('User.4447-by-me', storage.all())

    def test_save(self):
        """
        Test that an object is successfully saved to the database.
        """
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(self.new_user.id))
        result = cursor.fetchone()
        cursor.execute('SELECT COUNT(*) FROM users')
        old_cnt = cursor.fetchone()[0]
        cursor.close()
        dbc.close()

        self.assertTrue(result is None)
        self.assertFalse(self.new_user in storage.all().values())
        self.new_user.save()

        dbc1 = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor1 = dbc1.cursor()
        cursor1.execute('SELECT * FROM users WHERE id="{}"'.format(self.new_user.id))
        result = cursor1.fetchone()
        cursor1.execute('SELECT COUNT(*) FROM users')
        new_cnt = cursor1.fetchone()[0]
        cursor1.close()
        dbc1.close()

        self.assertFalse(result is None)
        self.assertEqual(old_cnt + 1, new_cnt)
        self.assertTrue(self.new_user in storage.all().values())

    def test_storage_var_created(self):
        """
        Test that DBStorage object storage is created.
        """
        self.assertEqual(type(storage), DBStorage)

    def test_new_and_save(self):
        """
        Test the new and save methods.
        """
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchall()
        cur.close()
        db.close()

        new_user = User(
            email='jack@bond.com',
            password='password',
            first_name='Jack',
            last_name='Bond'
        )
        new_user.save()

        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()
        cur.close()
        db.close()

        self.assertEqual(new_count[0][0], old_count[0][0] + 1)


if __name__ == '__main__':
    unittest.main()
