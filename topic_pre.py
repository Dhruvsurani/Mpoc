from google.cloud import pubsub_v1
import os

from google.pubsub_v1.types import pubsub

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/dhruvsurani/Downloads/miconcept-355405-88c28fcf47f4.json"
GOOGLE_PROJECT_ID = 'miconcept-355405'
TOPIC = 'projects/miconcept-355405/models/census'
# https://pubsub.googleapis.com/v1/{name}
publisher = pubsub_v1.PublisherClient()
topic_path = f"projects/{GOOGLE_PROJECT_ID}/topics/{TOPIC}"
# topic_path = publisher.topic_path(GOOGLE_PROJECT_ID, TOPIC)

publisher.create_topic(topic_path)