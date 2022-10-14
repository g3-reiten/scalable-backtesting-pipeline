from kafka import KafkaConsumer
from kafka.structs import TopicPartition

# To consume latest messages and auto-commit offsets
class KConsumerClass():
    """
    Consume records from a Kafka cluster.
    """
    def __init__(self):
        pass
    
    def create_consumer(self, topic_name):
        """
        Arguments:
                topics (str) – optional list of topics to subscribe to.
                                If not set, call subscribe() or assign() before consuming records.        
        """
        consumer = KafkaConsumer(bootstrap_servers=
                                 ["b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092"],
                                 api_version=(0, 10, 2)) #consumer_timeout_ms=60000 
        topic_partition = TopicPartition(topic_name, 0)
        assigned_topic = [topic_partition]
        consumer.assign(assigned_topic)
        return consumer
    
    def read_from_consumer(self, consumer):
        """
        run in loop?
        reading audio from kafka topic.
        
        audio is encoded as bytes
        
        using print() for big data results in IOPub data rate exceeded error
        """
        # other message properties -> message.topic, message.partition,                                
                                    # message.offset, message.key
        for msg in consumer:
            # send a value back to the caller
            # and continue execution immediately after the last yield run
            yield msg
        
    def get_subscribed_topics(self, consumer):
        """
        return topics that the consumer has subscribed to
        """
        return consumer.topics()
    
    def unsubscribe_from_topics(self, consumer):
        """
        unsubscribe from all topic
        """
        consumer.unsubscribe()


  