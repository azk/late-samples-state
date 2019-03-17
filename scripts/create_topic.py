from google.cloud import pubsub_v1
from os import environ

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(environ['GCP_PROJECT'], environ['PUBSUB_TOPIC'])
    # "staging-eabb77f6", "late-samples-state-test")

topic = publisher.create_topic(topic_path)

print('Topic created: {}'.format(topic))