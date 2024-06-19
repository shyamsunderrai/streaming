from confluent_kafka import Consumer, KafkaException
import json

# Kafka Consumer configuration
conf = {
    'bootstrap.servers': 'kafka-service:9092',
    'group.id': 'transaction-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to the 'transactions' topic
consumer.subscribe(['transactions'])

# Function to process messages
def process_message(message):
    try:
        transaction = json.loads(message.value().decode('utf-8'))
        print(f"Received transaction: {transaction}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

# Main loop to consume messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Wait for message or timeout after 1 second

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                # End of partition event
                print(f"End of partition reached {msg.partition()}")
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Process the message
            process_message(msg)

except KeyboardInterrupt:
    pass
finally:
    # Close the consumer to commit final offsets
    consumer.close()

