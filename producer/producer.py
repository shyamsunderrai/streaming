from kafka import KafkaProducer
import requests
import json
import time

producer = KafkaProducer(
    bootstrap_servers='kafka-service:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    response = requests.get("http://transactions:5000/transactions")
    transactions = response.json()
    for transaction in transactions:
        producer.send('transactions', value=transaction)
    time.sleep(5)  # Delay to simulate real-time data

