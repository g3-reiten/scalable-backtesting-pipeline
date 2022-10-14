from kafka import KafkaProducer
#from kafka.errors import KafkaError

import logging

class KProducerClass():
    """
    Create a Kafka producer and send messages to the topic in the cluster
    """
    
    def __init__(self):
        pass
    
    def create_producer(self):
        """
        Kafka client that publishes records to the Kafka cluster.
        """
        
        producer = KafkaProducer(bootstrap_servers=["b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092"],
                                retries=5)
        return producer
    
    def publish_message(self, producer, topic_name, value_bytes):
        
        """
        send() is Asynchronous by default. publishes a message to a topic
        
        Arguments:
                    topic (str) – topic where the message will be published
                    
                    key - partition to send the message to. If partition is None (and producer’s partitioner
                    config is left as default), then messages with the same key will be delivered to the same
                    partition (but if key is None, partition is chosen randomly). Must be type bytes, or be
                    serializable to bytes via configured key_serializer.
                    
                    value (messagevalue) - Must be type bytes, or be serializable to bytes via configured
                    value_serializer.If value is None, key is required and message acts as a ‘delete’
                    
                    timestamp_ms (int, optional) – epoch milliseconds (from Jan 1 1970 UTC) to use as the message
                    timestamp. Defaults to current time.
        
        Returns:
                    FutureRecordMetadata that resolves to RecordMetadata 
        Raises:
                    KafkaTimeoutError
                    if unable to fetch topic metadata, or unable to obtain memory buffer prior to configured
                    max_block_ms
        """
        
        try:
            # to convert text to Byte -> bytes(key, encoding='utf-8')
            # publish audio files as bytes
            message = producer.send(topic_name, value=value_bytes)
            # producer.flush()
            logging.info('Message published successfully.')
            return message.get()
        except Exception as ex:
            logging.error('Exception in publishing message')
            logging.error(str(ex))