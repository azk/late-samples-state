from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("staging-eabb77f6", "late-samples-state-test")

topic = publisher.create_topic(topic_path)

print('Topic created: {}'.format(topic))