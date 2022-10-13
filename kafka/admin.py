from ensurepip import bootstrap
from pydoc_data.topics import topics
from sys import api_version

from attr import validate
from kafka.admin.client import KafkaAdminClient
from kafka.admin import NewTopic

client = KafkaAdminClient(
    bootstrap_servers =["b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092, b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092"],
    api_version=(0,11,5)
)
print("API version:", client.config['api_version'])
print(client.list_topics())

topic_list=[]
topic_list.append(NewTopic(name="mela_topic", num_partitions=1, replication_factor=1))

client.create_topics(new_topics=topic_list, validate_only=False)
print("\n Topic created \n")
print(client.list_topics())
