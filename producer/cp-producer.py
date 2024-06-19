import requests
import json
import time
from confluent_kafka import Producer

# Define the REST API endpoint
api_url = "http://transactions:5000/transactions"

# Create the Producer instance
producer = Producer({
    'bootstrap.servers': 'kafka-service:9092'
})

# Define the delivery report callback to handle acknowledgment of messages
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Function to fetch transactions from the REST API
def fetch_transactions(api_url):
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

# Main loop to fetch data from REST API and produce to Kafka
while True:
    try:
        transactions = fetch_transactions(api_url)
        for transaction in transactions:
            producer.produce(
                topic='transactions',
                value=json.dumps(transaction),
                callback=delivery_report
            )
        # Wait up to 1 second for any outstanding messages to be delivered
        producer.flush()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    time.sleep(10)  # Wait before fetching data again to simulate real-time data

