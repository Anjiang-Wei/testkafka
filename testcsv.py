from kafka import KafkaProducer
import csv

# Define the Kafka topic and broker address
topic = 'my-topic'
bootstrap_servers = ['localhost:9092']

# Create a Kafka producer instance
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Read the CSV file and send each row as a message to the Kafka topic
with open('my-csv-file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Send the row as a message to the Kafka topic
        producer.send(topic, str.encode(','.join(row)))

# Close the Kafka producer
producer.close()

