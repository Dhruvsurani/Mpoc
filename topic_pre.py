from google.cloud import pubsub_v1

GOOGLE_PROJECT_ID = 'miconcept-355405'
TOPIC = 'dhruvsurani2000'

publisher = pubsub_v1.PublisherClient()
# topic_path = f"projects/{GOOGLE_PROJECT_ID}/topics/{TOPIC}"
topic_path = publisher.topic_path(GOOGLE_PROJECT_ID, TOPIC)

publisher.create_topic(topic_path)