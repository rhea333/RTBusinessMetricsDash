import unittest
from app import app, db, SalesData

class SalesDataTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_sales_data(self):
        response = self.app.get('/api/sales')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
