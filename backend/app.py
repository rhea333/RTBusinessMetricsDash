from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SalesData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(50), nullable=False)
    product = db.Column(db.String(50), nullable=False)
    sales = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

@app.route('/api/sales', methods=['GET'])
def get_sales_data():
    # Fetch sales data
    sales_data = SalesData.query.all()
    return jsonify([{
        "region": s.region,
        "product": s.product,
        "sales": s.sales,
        "timestamp": s.timestamp
    } for s in sales_data])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
