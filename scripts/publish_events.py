from datetime import datetime
import time
import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("staging-eabb77f6",  "late-samples-state-test")

def _create_event(key, val, ts=None):
    if not ts:
        ts = datetime.utcnow()
        
    return {
        "key": key,
        "value": val,
        "timestamp": time.mktime(ts.timetuple())
    }


futures = []

for k in xrange(10):
    for v in xrange(100):
        event = _create_event(k, v)
        print "send event: {}".format(event)
        message_future = publisher.publish(topic_path, data=json.dumps(event))
        futures.append(message_future)

print('Published message IDs:')
for future in futures:
    print(future.result())



