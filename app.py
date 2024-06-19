import random
import datetime
from faker import Faker
from flask import Flask, jsonify
from geopy.point import Point

fake = Faker()

def generate_transaction():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    longlat = Point(latitude, longitude)
    return {
        "transaction_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "transaction_date": datetime.datetime.now().isoformat(),
        "latitude": longlat.latitude,
        "longitude": longlat.longitude
    }


app = Flask(__name__)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = [generate_transaction() for _ in range(4)]
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

