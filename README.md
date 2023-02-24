# testkafka

## Download
```
wget https://dlcdn.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz
tar -xzf kafka_2.13-3.4.0.tgz
cd kafka_2.13-3.4.0
```

## Init with ZooKeeper
```
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties # another session
```

## Producer: Turn CSV into a Kafka Topic
```
# pip3 install kafka-python
python3 testcsv.py
```

## Consumer
```
bin/kafka-console-consumer.sh --topic my-topic --from-beginning --bootstrap-server localhost:9092
```
